import pandas
import json
import re
import sys
import re
import pickle

enterinput = raw_input()

output = []
metadata = enterinput

with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)
    #print b
    with open('filename2.pickle', 'rb') as f:
        d = pickle.load(f)



        if b.has_key(metadata) == 0:
             print "error:this is not such key."
        else:
             output.append(metadata)
             #print output

             while metadata != 0:
                  if b.has_key(b.get(metadata)) == 1:
                      metadata = b.get(metadata)
                      output.append(metadata)

             #for item in reversed(output):
                 #print item

                  else:
                      #if d.has_key(metadata[:-3]):
                      if b.get(metadata) == 0:
                          metadata = b.get(metadata)
                          output.append(metadata)
                      else:
                           metadata = metadata[:-3]
                           output.append(metadata)
                      #else:
                          #break

             for item in reversed(output):
                 print item







