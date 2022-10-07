sourcefiles=$(ls *.jemdoc)
python3 jemdoc.py -o www/ -c mesoler.conf $sourcefiles
