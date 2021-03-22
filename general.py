def fancy_print(text, separation='#'):
    '''
    print text in box surrounded by #
    '''
    text_len = len(text)
    if text_len>100:
        raise ValueError(f'{text} is too long for fancy_print')
    print(separation*(text_len + 8))
    print(f'{separation*2}  {text}  {separation*2}')
    print(separation*(text_len + 8))
    
def paragraph_print(paragraph, separation=None):
    '''
    print paragraph followed by an empty line or a line of separation signs
    '''
    print(paragraph)
    if separation:
        print(separation*50)
    else:
        print('\n')
        
def plot(data, plot_par, save_plot = False, save_par = None):
    '''
    save plots of segments
    plot_par is a dictionary with plot variables including [index] which can be any label associated to the segment, 
    in this case usually the start point of the segment
    save_par should have all the info including [name] and [location]
    '''
    assert not (save_plot and save_par is None), 'Provide save information!'
    
    #plot sequences, like waveforms
    if isinstance(data, list):
        plt.figure()
        plt.plot(data)
        
    #plot spectrogram
    elif isinstance(data, np.ndarray):
        fig, ax = plt.subplots(nrows=1,ncols=1, figsize=(20,4))
        cax = ax.matshow(np.array(data, dtype='float64'), interpolation='nearest', aspect='auto', 
                         cmap=plt.cm.afmhot, origin='lower')
        fig.colorbar(cax)
        
    if save_plot:
        setup.setup_folders(os.path.join(save_par['location'], 'plots'))
        plt.savefig(os.path.join(save_par['location'], 'plots', '%s_%s.png' %(save_par['name'], plot_par['index'])))
        plt.close()
        