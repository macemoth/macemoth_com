sourcefiles=$(ls *.jemdoc)
python2 jemdoc.py -o www/ -c mesoler.conf $sourcefiles