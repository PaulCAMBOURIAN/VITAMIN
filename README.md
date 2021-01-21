# Run
$ purr-data -inchannels 1 -outchannels 2 -send "filename <path/to/name>" -send "pd dsp 1" main.pd 
(where path/to/name is the path & name to the file where the settings and actions of the participant are being recorded)

# Note
abstraction "midi-id_to_internal-message.pd" reads in file "mapping". All other files prefixed with "mapping" are backup files. Consider copying one of them and rename as "mapping" to use any particular mapping.
