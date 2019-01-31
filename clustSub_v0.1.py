#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Cluster unique substitution

# version 0.1
# arahm@ucr.edu

# Set-up of holder
relapse = {}


# Go through input and prepare for reformatting
with open('Relapse.txt') as fh:
    for line in fh.readlines():
        line = line.strip().split('\t')
        if line[0] != 'CHROM':  # avoiding header
            k = line[1]
            if k not in relapse.keys(): # line[1] is START position
                relapse[k] = {'CHROM':line[0],
                       'START':line[1],
                       'END':line[2],
                       'REF':line[3],
                       'ALT':{line[4]},
                       'ANNOT':{line[5]},
                       'KARYO_GROUP':{line[6]},
                       'RISK_GROUP':{line[7]},
                       'RESPONSE':{line[8]},
                       'COUNT':1 # counter to track how many time a substitution happen in a position
                       }
            else:
                relapse[k]['ALT'].add(line[4])
                relapse[k]['ANNOT'].add(line[5])
                relapse[k]['KARYO_GROUP'].add(line[6])
                relapse[k]['RISK_GROUP'].add(line[7])
                relapse[k]['RESPONSE'].add(line[8])
                relapse[k]['COUNT'] += 1 # updating the counter
                
                
# Save output in new format
header = 'CHROM\tSTART\tEND\tCOUNT\tREF\tALT\tANNOT\tKARYO_GROUP\tRISK_GROUP\tRESPONS'

for d in relapse.keys():      
    new_line = '\t'.join([relapse[d]['CHROM'], relapse[d]['START'], relapse[d]['END'], str(relapse[d]['COUNT']), relapse[d]['REF'], 
    ','.join(relapse[d]['ALT']), ','.join(relapse[d]['ANNOT']), ','.join(relapse[d]['KARYO_GROUP']), 
    ','.join(relapse[d]['RISK_GROUP']), ','.join(relapse[d]['RESPONSE'])])
    
    # update line
    header = header + '\n' + new_line
    

open('Relapse_count.tsv', 'w').write(header)

         
                