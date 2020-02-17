#!/usr/bin/env python3

inIsland = "AATTACGTTTTACTGGTGTGCCGGGAGCCTGTAATTGGGCATCAGAACGTTCTGACAACACAACAGAAATGTTGTCATAATCCACATCGGCAAAACTATTCTTTAAGAAACGCTTGATATCGCTGATCTGATGCGCAAGCGGCGAACCTCGTTCATATACGGCTAATGCCGACAGATGAACAGGTTTTGGCGGGCGGCCATTTTCACCAGCATCAATATCATAACTAATATGGACCCTGGCGGAGAGCACGCCCTCCATCGTCTGTAATGACTGTTCCAGTCGCTGTTCAATAGCCGAATATAACCTGGCCTTTTCAGCTCGCGGAGACGATACCAGCGAATCCGCCGGGAACATCTGCGCTATTTCCACCCGTGGCCGGGGAGGAAGCTGATAAGTTTTAATCCAGTACACCGCAGCGGTAAAATCAGGCTCAGCAACGGTAATGCTATAGCCCAATTTTCCGCTATCAATTTTATTCGCCTCTATATTGTGCATTTGCAGAACGGCAATGACCTCATTAGCCTGTTCCTGGTCCAGTCCTTTTAAAAGATCCTTATCCTTACAGCCGGCAAGGGTCATTACCAGCAGAAAAGTATATAGATATCGACGAATCATGAGCGTAATAGCGTTTCAACAGCCCCGACTCCTTTACGAGTAAGGGTACTGACCATAGAAACATACAGGTTATAATCTGAAATCATCTCTTGCGAAATAGCCAGCTCTTTAGGATCCGTCACCAGATTAGGGTCCTCAATCCTGTTGGTAATCGTCTGTTTATCCACAGCCGTGGCAATCGCCGAACCAGAAAAAGCCTGGAGTAGCCGGTCATCCAGCGAGACAATGTCCGTTTCCATAGACCTGATATTGACCGCCTGCCCTATAACGGCATTCTCAGGGACAATAGTTGCAATCGACATAATCCACCTTATAACTGATTAACGGAAGTTCTGAATAATGGCAGCATCAATATCCTTAAAGACTTTTACCGTGTTCGATTGCGCGTTACGGTACAAGTTATATTCCGAGAGCTTACTCTGATACGCCGCCAGTAGCGCCGGATCGGAGGGTTTTGCTGCTAATTTATCCAGCGCCTCTGTTACCTGCGTTTGTAGATTATCAACGCCCGTATCAAATTTTGCTGAGACGTCATCCAGATAGCCTGACCAAGGTGTTGCCATAATGACTTCCTTATTTACGTTAAATTAAAGTGGGCTTGGGAAATACCAATGGCCTGGGCTCATTTTGATATAACCTTCCGCCCCGTACTGAAATGAGCGCCCCTTGAGCCAGTCATCTTTTAATTCGATCGCAAACTGCACATAGCGTCCTCCCCATGTGCGGTAATAGCTATCGACAAATTGACGGGCTCTGAGTATTTCTACATCATCGAGCGCCCCCTGAATAACAAACGTTACGCCCCCCTTATGATTCCTGCGGGAATAAGGTAACGCCTGCTGTTTTAGCCCCGCTTCCGCCTGGCCTGCTGCGGTAACATCGTCCATCAACGTGATGTTAACCGAATCCGCGTAAGGCATTAGCGCTCTCAGCTTTTGACTTAACACCTCGAGCTCTTTCTTGCTCATCGTGTTTCGCTGGCGGCTTAGCCAGAAAACGGGTTTACGCGGCTCATCGAAATGAATCCGATAATAAGCCAGCTGCGGATAATAGGTATCCAGCCAGATAGAGATACGCTTATTTTCTTCGTTTTCGTTAATCACTCGCGCATTTTTATCATAATCGCCCCTCGCTAAAACCTGACGAGCCCACAACGTATCTCTTTCATTTTGCGCAGCGACATAGAGCATTTTGTCCCGGCCTGGCAACACCTGAAAACGCTCCTTCTCCTGCCCCAATAACGAATCGAGCTCTGCGGCCTGCCGCTGCGGCGAGTTAAGTATCCATAACGTCCCCACAGTCCCAATTCCCAATATAAAAAACCCGGCCAGTGCTGCTACAATTCCGTTTTTAAAACGCGGCTCGTTCTTTTTTGCAGACGTTTCTAACTTCTCAGGCTGCTCGGGCACCCACGGCTCGCTTTCCGGGCGAATCAGGATAAGCAATTCACCGACCTGTATTGGCGTATTTAATTGCACCGAACGAGATTCAGAATTTCCTTCTTTCAGCTCATGGAGTATAATTTCGGTCGCATCCGTATCCACCTGGATTTCAAAATTTACTCCGCCATGGTCCAGCGGGATAAAAAAGCTATCGGCAGGTATATCAGGGAGTTGACCTGAAGCAGTGAGCGCATCACTCTGACCTACCACAAAGAGTGTTCGGCCTGTCAGCAATGGAAACTCACAGCCGTTCAGTGAGCTGTTAAGTAATCGAACTATGTATGGCCCTGGGCTTGTTATCGTCTTCTCTTTTGATGTTTCCATATATACTGTTAGCGATGTCTGTCGTTCTCGATAGCAGCAGATTACCGCACAGGACACAGGGATTCCTGATGAAAATAGAATGAAAAGTGAGAAATAAAATCAATTTATTCTGTATAATGCGTCTCAACACATATTAAAAGAACCATCATCCCCATTGGGGCTTAAACTACTGTAGATAAATTACCCAAATTTGGGTTCTTTTGGTGTAACAATCAGACCATTGCCAACACACGCTAATAAAGAGCATTTACAACTCAGATTTTTTCAGTAGGATACCAGTAAGGAACATTAAAATAACATCAACAAAGGGATAATATGGAAAATGTAACCTTTGTAAGTAATAGTCATCAGCGTCCTGCCGCAGATAACTTACAGAAATTAAAATCACTTTTGACAAATACCCGGCAGCAAATTAAAAGTCAGACTCAGCAGGTTACCATCAAAAATCTTTATGTAAGCAGTTTCACTTTAGTTTGCTTTCGGAGCGGTAAACTGACGATTAGCAATAATCACGATACGATTTACTGTGACGAACCTGGGATGTTGGTGCTCAAAAAAGAGCAGGTAGTTAACGTGACGCTTGAAGAGGTCAATGGCCACATGGATTTCGATATACTCGAGATACCGACGCAACGACTTGGCGCTCTCTATGCACTTATCCCAAACGAGCAGCAAACCAAAATGGCGGTACCCACAGAGAAAGCGCAGAAGATCTTCTATACGCCTGACTTTCCTGCCAGAAGAGAGGTATTTGAACATCTGAAAACGGCGTTCTCCTGTACGAAGGATACAAGCAAAGGTTGCAGTAACTGTAACAACAAAAGTTGTATTGAAAATGAAGAGTTAATTCCTTATTTTCTGCTGTTCCTGCTTACTGCTTTTCTCCGACTCCCGGAGAGTTATGAGATCATCCTTAGCTCGGCTCAGATAACGTTAAAGGAGCGCGTTTACAACATTATATCTTCGTCACCCAGTAGACAGTGGAAGCTTACGGATGTTGCCGATCATATATTTATGAGTACGTCAACGCTCAAACGGAAACTTGCAGAAGAAGGTACCAGCTTTAGCGACATCTACTTATCGGCAAGAATGAATCAGGCAGCAAAACTTTTACGCATAGGCAACCATAATGTTAATGCTGTAGCATTAAAATGTGGTTATGATAGCACGTCCTACTTCATTCAATGTTTCAAAAAATATTTTAAAACTACGCCATCGACATTCATAAAAATGGCGAACCATTAACATTTTTTGTATCTGTCACTTAAGTAAAGATTTTTATTAAAATTGTAATAATTTAAAATTCAGACTGCGCATTAACACGCTCTATCAGGATGGGAGGCTATTCAATATCATTGTTCTGTCCGGAAGACAGCTTATACTGATATCTATGGTAATTTAAAGTAAGGCTGATTATATAACACGATTTTTGTGAACTTGTCATCGCTATGATGACTGGTAAAACGATATTGCCTTATTCACAGCGTAAGAATTCGTCCAGATGACACTATCTCCTTCCGGCTTTAACCCTGTGGATTAAGGCCGGCATTTTATTCATATTTATACATCATCCGTTCCCTCTGAGAACTATTTGCCTGAACGGTTTATACCGAAACAGTCACGCTTGTTAGCTTTCTGCCAGGCATACCTCCTCTCTTCCTCCTGATATCGATATAATGCCTGGAGCCAGCCTGAGGATGATACTGCTCATAACCCTCCTGCCTTTTTGACGCTATAACTGAAGGGAGTAAAGAAAAGACGATATCATTATTTTGCAAAAAAATATAAAAATAAGCGCACCATTAAAAACAGTCTTTCATTTATATTTTGGAACCTAAGACAAATTACACTCTTAAACTTTCAACGAATGGTCATTTAGTGGAAATCTTCGAGAAAAATGGTTCTGATGGTGTAATTATCAGACCATTAACCATGAAGATATAATAAGCAGCATTTACACCCCAAAAAAATGCAGTAAGATAGCTACAAAACTAATCTCTATTGCAATGAGGCCAAGTTAAATATGTAAATATTTAGATGCCCGGCGCTGACTCTCTCTGCACCAGGATATACGGCAGCGTCCATTCGATAATCACAGTTAGTTATAACAATATTATTACCAACATGTCAGTTATTTAAAGCACAGGCATAAGCTAAATAATCAAATGTTAAAAACATATAAACCCGAGCCCGTAGAATATGACATTAAGCTCATAATAAAAGCTCAACCTGACCGTTAGTACTAACAGCAGAATTACTGAAACAGTAGATTCTATCCTAACGACTTGTATTAGTTATTATAACTTTTCACCCTGTAAGAGAATACACTATTATCATGCCACATTTTAATCCTGTTCCTGTATCGAATAAAAAATTCGTCTTTGATGATTTCATACTCAACATGGACGGCTCCCTGCTACGCTCAGAAAAGAAAGTCAATATTCCGCCAAAAGAATATGCCGTTCTGGTCATCCTGCTCGAAGCCGCCGGCGAGATTGTGAGTAAAAACACCTTACTGGACCAGGTATGGGGCGACGCGGAAGTTAACGAAGAATCTCTTACCCGCTGTATTTATGCCTTACGACGTATTCTGTCGGAAGATAAAGAGCATCGTTACATTGAAACACTGTACGGACAGGGCTATCGGTTTAATCGTCCGGTCGTAGTGGTGTCTCCGCCAGCGCCGCAACCTACGACTCATACATTGGCGATACTTCCTTTTCAGATGCAGGATCAGGTTCAATCCGAGAGTCTGCATTACTCTATCGTGAAGGGATTATCGCAGTATGCGCCCTTTGGCCTGAGCGTGCTGCCGGTGACCATTACGAAGAACTGCCGCAGTGTTAAGGATATTCTTGAGCTCATGGATCAATTACGCCCCGATTATTATATCTCCGGGCAGATGATACCCGATGGTAATGATAATATTGTACAGATTGAGATAGTTCGGGTTAAAGGTTATCACCTGCTGCACCAGGAAAGCATTAAGTTGATAGAACACCAACCCGCTTCTCTCTTGCAAAACAAAATTGCGAATCTTTTGCTCAGATGTATTCCCGGACTTCGCTGGGACACAAAGCAGATTAGCGAGCTAAATTCGATTGACAGTACTATGGTTTACTTACGCGGTAAGCATGAGTTAAATCAATACACCCCCTATAGCTTACAGCAAGCGCTTAAATTGCTGACTCAATGCGTTAACATGTCGCCAAACAGCATTGCGCCTTACTGTGCGCTGGCAGAATGCTACCTCAGCATGGCGCAAATGGGGATTTTTGATAAACAAAACGCTATGATCAAAGCTAAAGAACATGCGATTAAGGCGACAGAGCTGGACCACAATAATCCACAAGCTTTAGGATTACTGGGGCTAATTAATACGATTCACTCAGAATACATCGTCGGGAGTTTGCTATTCAAACAAGCTAACTTACTTTCGCCCATTTCTGCAGATATTAAATATTATTATGGCTGGAATCTTTTCATGGCTGGTCAGTTGGAGGAGGCCTTACAAACGATTAACGAGTGTTTAAAATTGGACCCAACGCGCGCAGCCGCAGGGATCACTAAGCTGTGGATTACCTATTATCATACCGGTATTGATGATGCTATACGTTTAGGCGATGAATTACGCTCACAACACCTGCAGGATAATCCAATATTATTAAGTATGCAGGTTATGTTTCTTTCGCTTAAAGGTAAACATGAACTGGCACGAAAATTAACTAAAGAAATATCCACGCAGGAAATAACAGGACTTATTGCTGTTAATCTTCTTTACGCTGAATATTGTCAGAATAGTGAGCGTGCCTTACCGACGATAAGAGAATTTCTGGAAAGTGAACAGCGTATAGATAATAATCCGGGATTATTACCGTTAGTGCTGGTTGCCCACGGCGAAGCTATTGCCGAGAAAATGTGGAATAAATTTAAAAACGAAGACAATATTTGGTTCAAAAGATGGAAACAGGATCCCCGCTTGATTAAATTACGGTAAAATCTGAGAGAGGAGATATGCATTATTTTTTTATCATCGTAATCTGGTTGCTTAGCATAAATACGGCATGGGCTGATTGCTGGCTTCAGGCTGAAAAAATGTTCAATATTGAATCCGAACTACTTTACGCTATCGCCCAGCAGGAATCGGCGATGAAACCTGGCGCCATTGGTCATAACCGAGATGGTTCAACCGATCTTGGCCTGATGCAAATTAACAGCTTCCATATGAAAAGGCTGAAAAAAATGGGGATTAGTGAAAAACAGTTGTTACAGGACCCCTGCATTTCTGTCATTGTGGGCGCCTCCATTTTATCAGATATGATGAAAATCTACGGTTATAGCTGGGAGGCCGTTGGCGCTTATAATGCCGGGACGTCGCCGAAACGATCGGATATAAGGAAACGTTATGCTAAAAAAATTTGGGAGAATTACAGAAAATTAAAAGGAATGTCAGCAGAAGAGAAAAACAAAAGACTTTCTATCGCGGCAAACAAATAATTATACAGAAATAGCTTACTTTCAGATAGTTCTAAAAGTAAGCTATGTTTTTATCAGCTTGCCGTCGTCATAAGCAACTGGGCTTGCATTGCTTTTAGTTGTACAAACTGTGAGGCGTCTTCCAGCATTCTATTGTTCCGTGAATCCCGGAAATCTGCACGTACCTGCTCCAGATTACTATGAGGATTATCCTTAAGTACAAGGGCCGCCGCCATCGTTCCGGTTCTTCCCACTCCGCCCAGACAATGAATCATCGGTAAATGCTTATCTGATGAACTACGCCCCGGCGCGCCATTTTGGTTACTATTTTTCACCCTATCCGCCAGGTATTCTAACTGATCCGTAGACGGTAACGGCTGGTGATCTGGCCAATTTTTCACATGCAATACCGGGATTGTATACCGCTTTTCCCCGCAGGACAGTTGCATATTGTATTGGTCTATCGCTTCTCCCTGACTGGCTGAGCTCACTTTTTGGCTGTTGGTATGCACCTCGCCAAAGGTGTAGCTCCCTCTGAAATAGGGTGGTAATTGTTTTGCCTGCATCTGATCTTCCGACGTTAACACCACCAGGCACGAGCATTCTTTTTCAAGAAGCATTTTCATATGCGCTTCCAGCGCATCCGGCGTATTTTTTGGGTACGAACCGGCTAATGCCACAGGCTTACCGTCAAAAGTTAACGTATTCACTGGCACAGGCATTCCATCGCTCAGTTTCACCTGGGTTTGCTGATTAATTGGAATGCTGCTGACCGCAAATCGTGCCAGGCCCAGTGTCGGTCCGCTCATCGTCTGTGGCATTGGCGCGCCGGCTTCTATTTTCTCAAGTTCAGCTGTAACATTTTTCAGTTCTTTAGCAATAACGTGAATTTTTTTTACAGCCTGGGTTAATTCATGAGTAGAGGCTTTATCAACCCACCTCTCAACCTCTCCTCCACAGGTTCCCCATTGTGAGAACCGGGCTACACCGACCTGAATATTTGTTAACGTTGTAACATAATCATTAAGTTGTTTAGCCTCTGGAATTTTATTTAAATTCTGTAAATTCGTCATTAATGAACGCAGCGGGCCGTTACCTGAAGCCATCTCCTGGAAGTTTTCTCGCAGGCTATTTCCATCCATTTGTTCCAGTTGCGGTAATGTTCTTTTAAGTCCCTTTAGCGCGATATCGAGTAAAGGTTGCTTACTTTCTGCTCCAACATCGTTATTTTTTTCTGCCACTTTTGTATCGCCGCCTTTTATGACTAAAGCGGCATTCCTGACACCAACATTATCCTTGCTCTTAATAAGGTTTATAAACCCTTCGTCAGCAGCTTTTACACACTCCGTGATCTGCACTGCTAAACGTTGGGTAAGGGGTTTGTTCATATTTATACGGGACATTAACAGTGCGTCATTAACCGCTGTTTCCCCATATTTTTCCGTTAGTGCATGGAGAAATGTCTGTAAAATCTTTTGGTCCTGTACTCTGATATTTTCCGTATGTTTTTGCACCACTTCAGTGTTTTTAAATAACGGCATTTTTCCAAGCCAGGTTAATACTTTTGACGAAAATTTTTCAGGCGCAACATATGCCTTATCAGTATTTTCCTTAGCAATATAAAGTCGGGCATCATTCGACACACCAACTTTTGAAAACGAAGACAACGTTAAATTATTCAATTTTCTCTCCTCATACTTTAGCATATTCCTGCAGTATGTTTTTGAGCGCTTCCTGCTGATTCACAAATGACTCAAGCTGCGATATAATATGGTAAGTATTTGTCAGATCGGTAATTGCATGTATAAGCAACAACGTCTCTGCGGCATCAATATACGCTAACGTACCTTCATTATTCGCAGCCAGTTCACCATTAATCACCATAATCTGCCGCCAGATAGAATCGCCACAAACAGGCGATAACGGTATAATCATACCGTTCAATAACCAGATATCATCTTTAGCTTCAATAGACGTAAAAATATCGCTATCGAGTAATAATAAGCACTGATTGTTGTCGTCAAAAGTGAGCGGTAAACCCAATTTCTCACCAATATTAGCGATAATATCCTGGTGTGCTTGCAATTTACTTTCCTCTTGAATTATATCTTTTATAAGATTGCTTCTTCAAATTTAATCTGGTTACACAATGTCTTGATACTTTTTCGCGCCCATCGCCGGGCGCAATATTTCTCTCCTTTAATCCAGTAGAATAGCCATTCACTACGCATCGGAACACATATCAGCAGCTCCTTCGGATCATTTTCAACATGACGTAACTTGCCTTTAATAACAAAACGCGAACTGTCAGCAATATCATCATATATTGCAGCCATACCTGAACCGGGTACTACATGTGTGATGATTTTCATAACAATTAATCTTATTCAATTGTTGTCAAGCGAGAGAAAAATACTACACCCTGGACTCAAGACTTTTTTTAACAACACGGCATATATCCGCAAAGGTCATCATATCAGGAAGATCGTTTTCATTGCAACTAATGTCAAACTCCTCACTAAGACCAAATACAATATCAATTAAATCCAATGAGTCAGCGTAAAGATCCTCAACCAGATGGGTCTGACCATTGATACTATCAACATCAACGGCAATACAAGAGGTGATCACTTTTTTGACTCTTGCTTCAATATCCATATTCATCGCATCTTTCCCGGTTAATTAACGCTGCATGTGCAAGCCATCAACGGTAGTAATAACCCGATCCACGCCAGGTTTATTCAGGTATGACTCGTAAGCCGGGCCAGCTCGCCAGCTACCGTCTCCGATAAGGCCGTCCAGCACATTACTTAACACATAGTCAGTTTCCCCTTTTAGCCTGGTCAGCCCCGCCTCTCTGGCAAACTGCAGTGCAATCTCAGCCAGTTTTTCTTTTTGTGGATGATGAGTAATGACCTCTTTGAGAGTCTCCATTTTCGCTTTCAATTCTGGGTGCTTGTCAATATCGCTACATTGCGCTTTCAACGCTGCACTCTTTATCGTGTCATTGGGTAATATTTCCGCACGCAAGCCGTCAAACGCTCTGCGTACAGGGAACGGTGTGGAGGTATCTGGCTCCAGGGCTTTACGTATCACACCCAAAAACGTCTCACGGGCGTCGAAATGCATTGAATGCATATTC"
outsideIsland = "GGCCTGCTTAAACGGCGCGGCGATTTTGTTTTTCACCACTTTCACACGCGTTTCGCTACCCACGACATTATCGCCCTCTTTCACCGCGCCAATACGACGGATATCAAGACGAACAGAGGCGTAGAATTTCAGCGCGTTACCGCCGGTGGTGGTTTCCGGGTTACCGAACATCACGCCAATCTTCATACGGATCTGGTTGATGAAAATCAACAGCGTGTTGGACTGTTTCAGGTTCCCCGCCAGCTTACGCATCGCCTGGCTCATCATACGCGCCGCGAGGCCCATGTGAGAGTCGCCGATTTCGCCTTCGATTTCCGCTTTCGGCGTTAGCGCCGCTACGGAGTCGACCACAATGACGTCCACCGCGCCTGAACGCGCCAGCGCGTCACAGATTTCCAGCGCCTGCTCGCCGGTATCCGGCTGAGAGCAGAGCAGGTTATCGATATCGACGCCCAGCTTGCGTGCGTAAACAGGGTCAAGCGCGTGTTCCGCATCGATAAACGCACAGGTTTTACCTTCACGCTGCGCAGCGGCAATCACCTGCAGCGTCAGGGTCGTTTTACCGGAAGATTCCGGCCCGTAAATTTCGACGATACGCCCCATCGGCAGACCGCCCGCACCGAGTGCGATGTCCAGTGAAAGCGAACCGGTGGAGATAGTTTCCACATCCATAGAACGGTCTTCACCCAGACGCATGATGGAGCCTTTACCAAATTGCTTTTCAATTTGGCCCAGTGCTGCCGCCAACGCTTTCTGTTTGTTTTCGTCGATAGCCATTATTACTCCTGTCATGCAACTTGGTATTGAACCGGATAGTGAATTCGTACTGTTGAAGCAATTATACTGTATGCTCATACAGTATCAAGTGTTTTGTAGAAATTGTTGCCACAGGGTTTGTAGCGCGTATGTCGTCGCCTGTCGACGCACCGATTCACGGTCGCCGCTGAAGCATTCCCGACGCGTAATCCCTTCTCCACTGACGCTGGCGAAAGCAAACCACACCGTACCAACCGGCTTTTCTTCACTGCCGCCATCCGGCCCGGCAATCCCGCTAATAGCGACAGCAAAATCGGCGCGAGCGGCCTTCAGCGCCCCGATCGCCATTTCGACCACTACGGGTTCGCTGACCGCGCCATGCTGCGCCAGAGTCTCTTCACGCACGCCAATCATCTGCGCTTTGGCTTCATTACTATAGGTGACAAAGCCGCGTTCAAACCAGGCGGAACTTCCGGCGATGTCGGTAATGGCTTTCGCCAGCCAGCCGCCGGTACAGGACTCTGCTGTCGTTACGGTCGCCCCGCGCGCTTTTAACGCCAGCCCGACCTGCTCGCTAAGCCGCATCAGTTCACTGTCAGTCATCATGACCTCTGTCAGTTAGAAATCCTGCCGCACAAGATAGCACTTTCTCACCAGAGATGGGGACGAGCTGTCGATTTTACGAGTCGGATTCCGAAAAAATGCCAGCAGGTTATTTATGCAGAATGAAAGAGGTAGCACTTGACTAAATAGCAGTACCATGTCGCTAAATTTACACGTACGGAGAGAAAGCAAGGATGTCACTCAAAAAAACGGAAAGCACACAGCACAAACTGAAACAAACCTGTCAACTACGGCTGTGGTTAATTGTGGGTGGAGTATGTTCATTAGGAATGGGAGTACTGAATATATTGTCGTCAGGCTATTTTGAACCGTATGACGGCGGTCAAATTATCTTAGGCCTGGGATGTCTGGGATATAGTCTGGCACTATCAAAGAAGATATCCCACTTGCAGGCAGAGAATCAGCCCAAAAAGCCATAATAATAGCGGAGGGGGTGCTCCCCTCCCTAAGCGTAAATTAGCGCACCCGCGCCAGCGCTACCGCCTGGCCCAGTTGCCAAACCGCCATCGCATAATGCGTGCTGTGGTTATATCGGGTAATTGTGTAGAAGTTCGGCAGGCCGTACCAGTACTGGTATCCCGTACCGATATCCAGACGCAGCAGGCTGGCTTCCTGATGATTGCCCAACGATTGCTGCGGCGTTAAGCCTGCGGCGGCAAGCTGAGAGATGCTGTATTTTGTTTTGAAACCATTCGCCAACCCAGGCGCCTGACCACTCGCCGGCACCGCAACCATATCGCCTTTCACCCAACCATGCGCCTTGAAATAGTTCGCCACGCTGCCGATGGCATCTACCGGATCCCACAAGTTAATGTGCCCATCACCATTGAAATCGACCGCATATTCTTTATAGGAAGATGGCATAAACTGGCCGTAGCCCATCGCGCCCGCAAAGGAACCTTTCAGATTGAGCGGATCGTCTTGCTCATCGCGCGCCATGAGCAGGAAGGTTTCCAGCTCGCCGGAGAAATATTCCGCCCGGCGCGGATAGTTAAATGACAGCGTCGCCAGCGCGTCCAGAATCCGCGTTTTCCCCATGATACGTCCCCAGCGGGTTTCCACGCCGATGATGCCCACGATGATCTCCGGCGGTACGCCGTATACCTGCCAGGCGCGGTTCAGCGCGTCTTCATACTGATTCCAGAACGCGACGCCGTTTTGCACGTTATCCGGCGTAATAAATTGTTTGCGGTAGCGCAACCAGGCGCCATTTGGTCCGGCGGGCGGCTGAGTGGTCGGCGCTTGTCTGTCCATCAGACGCAGGACGTAATCCAGTCTTTTAGACTGCGAGAGGATCTCTTGCAACTGCTGACGGTCGAAACCGTGTTTACTGACCATTTTATCAATGAACTGCTGCGCATTAGGGTTGTTGGCGAAGTCGCCGCCCATTTGCATGACGTTATGCTGCGGCTCAAGCAGAAAGCCGCCGGAAGGCGTGCCCGTCGTCGCTTGAGTCTCGGAAGATTTTGGCGTGCTGCTACAGGCAGCAAGCAATACGCAAAGTGGAAGTAACGCTACATAACGACGCTTGAACATGAGACATCCATTAAACAAATTCAGCCAGGGAGAAGTATGGTAAAGCATCCCCCGCCGCACAAGGAAGCGGCACAAGAGAATAAATCACCTTTCTCCTCTTTTCAGTTTGTATACGCTCCCTCACTCCCACAATCTTTCAATTTAAAATATTTTTCTTTTATTTTGCGATCACAATAACACTTTTAAATCTTTCAACATGATTACAATGAACAGGAAATTAGCAAGAAAACTAAAAACCCTACAGGAGAGAACAATGATCGAAACCATTACACATGGTGCGGAGTGGTTCATCGGGTTATTCCAGAAAGGCGGAGAGGTGTTTACCGGTATGGTGACAGGTATTCTTCCGCTACTGATAAGCCTGCTGGTTATCATGAATGCGCTCATCAATTTTATCGGCCAGCAGCGTATTGAGCGTTTTGCCCAACGTTGTGCCGGAAATCCGCTATCTCGTTACCTGCTTTTACCGTGTATCGGGACATTTGTTTTTTGTAATCCGATGACCCTGAGTTTGGGACGCTTTATGCCGGAGAAGTACAAGCCGAGCTATTACGCGGCGGCCTCCTATAGCTGTCACTCCATGAACGGTCTGTTTCCGCATATCAATCCCGGCGAACTGTTTGTTTATCTGGGGATCGCCAGCGGACTCACCACGTTAGGGCTTCCTCTCGGCCCGCTCGCGGTGAGCTATCTGCTGGTAGGTCTGGTGACGAACTTCTTCCGCGGTTGGGTCACCGATCTCACCACCGCTATTTTTGAGAAAAAAATGGGGATTCAACTTGAGCAGAAAGTTCATCTGACAGGAGCGGTATCATGACACGGGTTCGCATTGAGAAAGGCGCCGGCGGCTGGGGCGGCCCGCTTGAACTGGACGTTACGCCAGACAAAAAGATCGTCTATATCACAGCCGGTACGCGCCCGGCGATCGTCGACAAACTGGCGCAACTAACAGGCTGGCAAGCGGTGGACGGCTTTAAAGAAGGCGAACCGCCGGAAGCGGAGATCGGCGCGGCCATTATCGACTGCGGCGGTACGCTGCGCTGCGGTATCTATCCGAAACGCCGGATTCCAACCATTAATATTCACTCGACGGGTAAGTCCGGCCCACTGGCGCAGTATATTGTTGAGGATATTTATGTCTCCGGCGTAAAAGAAGAAAACATTACTCTTGTCGGCGAAACGCCTGCCAGTCCCCAGCCTGCCAAAACGACATTAGGACGTGACTACGACACCAGCAAAAAAATCACCGAGCAGAGCGACGGGCTGCTGGCAAAAGTCGGTATGGGAATGGGCTCCGCCGTGGCGGTACTGTTCCAGTCCGGTCGCGACACCATTGATACGGTCCTGAAAACAATCCTGCCGTTTATGGCGTTCGTTTCGGCGCTGATCGGCATCATTATGGCCTCAGGTCTTGGCGACTGGATCGCCCACGGCCTGGCGCCATTAGCCAGCCATCCACTGGGGCTGGTGACGCTGGCATTGATCTGCTCGTTCCCGCTGCTGTCGCCCTTTCTCGGCCCTGGCGCGGTTATCGCTCAGGTCATTGGCGTCCTGATCGGCGTTCAGATAGGCCTGGGCAATATCCCCCCGCATCTGGCGCTTCCCGCCCTGTTCGCGATTAACGCGCAGGCGGCCTGCGACTTTATCCCGGTCGGCCTGTCGCTGGCGGAAGCGAAACAAGACACCGTTCGCGTCGGCGTACCTTCTGTGCTGGTCGGACGCTTCCTGACTGGCGCGCCCACGGTACTTATCGCCTGGTTTGTTTCCGGCTTTATCTATCAATAAGAGGTTCAGACATGAGCGTGATTTATCAAACCACCATCACCCGTATCGGCCAGAGCGCGAAGGAAGCGCTCGGCGAACAGATGCTGATTACGTTTCGGGAAGGCGCGCCGGCGGATATCGAAGAATTTTGCTTCATCCATTGTCATGGCGAACTGACCGGCGCGCTGCAGCCTGGCGCGCGGTGTGAATTGGGTCAACATTGCTATCCGGTCACGGCGGTCGGCAGCGTAGCCGAGCAAAACCTGCGTGAACTGGGGCATATCACTTTGCGCTTCGATGGTCTGCGTGAAGCGGAATTTCCCGGCACCGTACACGTTGCGGGGCCTGTACCGGACGATATCGCGCCGGGCTGTATTTTGACGTTTGTCGCTTAAGGAGAAAAAACATGAATCAAGTTGCCGTTGTCATTGGCGGAGGCCAGACCCTGGGGGCATTCCTTTGCCGTGGGCTTGCAGAAGAAGGATACCGCGTGGCGGTCGTTGATATTCAAAGCGATAAAGCCGCGAATGTCGCCCAGGAAATTAACGCCGATTTTGGCGAAGGTATGGCGTACGGTTTTGGCGCCGACGCCACCAGCGAGCAGAGCGTGCTGGCGCTTTCCCGCGGCGTAGACGAGATTTTCGGGCGCGTCGATCTGCTGGTTTACAGCGCGGGTATCGCCAAAGCGGCGTTTATCAGCGATTTCCAGTTGGGCGATTTTGACCGCTCGCTACAGGTGAATCTGGTGGGCTATTTCCTCTGCGCCCGTGAGTTTTCCCGCCTGATGATCCGCGACGGCATTCAGGGGCGCATTATTCAGATTAACTCTAAATCCGGCAAAGTGGGCAGTAAACACAACTCCGGCTACAGCGCGGCGAAATTCGGCGGCGTGGGGTTAACCCAGTCTCTGGCGCTGGATCTGGCGGAATACGGCATTACCGTACACTCGTTGATGCTCGGCAACCTGTTGAAATCGCCGATGTTCCAGTCACTGCTGCCGCAATACGCCACTAAACTGGGCATTAAGCCCGATGAGGTGGAACAGTATTACATTGATAAAGTACCGCTCAAACGCGGGTGTGATTATCAGGATGTGCTGAACATGCTGTTATTTTATGCCAGCCCGAAAGCGTCTTATTGCACCGGGCAGTCGATCAACGTAACCGGCGGTCAAGTGATGTTCTGACCGTGAATTGCCGGATGGCGCCGTAGGCCGGATAAGACGGTTACGCGCCATCAGGCAAAACAACAGGAGCACATTATGGTTTCCACTCTGATTACCGTCGCCGTTATCGCCTGGTGTGCGCAGCTGGCGCTGGGCGGCTGGCAGATTTCCCGCTTTAATCGGGCTTTCGATAAACTTAGCCAACAGGGGCGGGTCGGCGTCGGGCGCTCCGGCGGGCGTTTTAAGCCCCGGGTGGTGGTTGCCGTGGCGCTGGACGAACAGCAGCGGGTGACGGACACTTTATTGATGAAAGGCCTTACGGTATTCGCCAGACCGGTTAAAATTGCCGCAATGCAAGGAAAACATTTGCATGAATTACAGCCTGATGTGATCTTTCCCCATGATTCGCTCGCGCAGAATGCACTATCATTGGCGCTTAAACTGAAACATGGGTAATTTCGTTGTGAATGCGTATAGCTTGCGAAATTATCATTTTGCAACCAATACCCTAAATAATTCGAGTTGCAGGAAGGCGGCGACGCAGCGAATCCCAGGAGCGTACATCAGTACGTGACCGGGGTGAGCGAGGAAAGCCAACGCACATGCAGCGTGAAGTATGACGGGTAAATACATAAGTCAGGGTAATCACGCCTATGAAACCTCGTCAGCGTCAGGCCGCGATTCTGGAGCACCTGCAAAAACAGGGAAAATGCTCGGTTGAAGAACTGGCCCAGTACTTTGACACGACAGGCACCACTATCCGTAAAGATCTGGTCATTCTGGAAAATGCCGGAACCGTCATCCGCACCTATGGCGGCGTGGTGTTGAATAAAGAAGAGTCCGATCCGCCTATTGATCACAAAACGCTTATCAACACCCACAAAAAAGCGCTGATAGCCGCAGCCGCTGTGAAATATATCCATGATGGCGATTCCATTATTCTGGACGCCGGAAGTACCGTGTTACAGATGGTGCCGTTGCTTTCGCGTTTTAGCAACATCACGGTGATGACCAACAGCCTCCATATTGTTAACGCGCTATCGGAACTGGACAACGAACAAACTATCCTGATGCCCGGCGGCACCTTCCGTAAAAAATCGGCGTCGTTTCACGGTCAACTGGCGGAAAACGCCTTTGAGCAATTCAGCTTTGATAAACTTTTCATGGGAACTGACGGTATTGACCTGAATGTCGGTGTGACCACGTTCAATGAGGTTTACACCGTCAGTAACGCAATGTGCAATGCAGCACGCGAGGTGATTCTGATGGCGGACTCCTCAAAATTTGGTCGTAAAAGCCCCAATGTGGTGTGCAGTCTGGAAACCGTCGACAAACTGATCACGGACGCGGGGATCGATCCGGCATTTCGTCAGGCGCTGGAAGCAAAAGGGATTGAAGTAATCATAACCGGAGAAAGCAATGAGTGATGCACTACTAAACGCGGGCCGTCAGACCTTAATGCTGGAGCTACAGGAAGCCAGCCGTCTGCCGGAGCGTCTGGGCGATGATTTTGTCCGCGCCGCCAATATCATTATTCACTGTGAAGGCAAAGTGATCGTTTCCGGTATTGGTAAATCAGGTCATATTGGTAAAAAAATCGCCGCGACGCTTGCCAGTACCGGTACTCCCGCTTTTTTTGTTCATCCGGCGGAAGCACTGCATGGCGATCTGGGGATGATTGAAAGCCGCGACGTGATGTTATTTATCTCCTATTCCGGCGGCGCAAAAGAACTCGACCTCATCATCCCGCGTCTGGAAGATAAATCCGTCGCGCTGCTGGCGATGACCGGTAAACTTCACTCTCCGCTGGGGCGAGCGGCAAAAGCCGTTCTGGATATTTCCGTCGAGCGTGAAGCCTGCCCGATGCATCTGGCGCCGACATCCAGTACCGTCAATACGCTGATGATGGGCGATGCGCTGGCGATGGCGGTCATGCAGGCGCGCGGTTTTAACGAAGAAGATTTCGCCCGTTCGCATCCGGCTGGCGCACTGGGCGCGCGTTTGCTCAATAATGTGCATCACCTGATGCGCCAGGGCGATGCAATACCGCAGGTGATGCTTGCCACCAGCGTGATGGATGCCATGCTGGAACTTAGCCGTACCGGGCTGGGGCTGGTGGCGGTTTGCGATGAGCAACATGTTGTGAAAGGCGTCTTTACCGACGGCGACCTGCGTCGCTGGCTGGTGGGCGGCGGCGCGCTCACCACGCCGGTAAGCGAAGCCATGACGCCCAACGGTATTACGCTCCAGGCGCAAAGCCGCGCCATTGACGCCAAAGAGCTCCTGATGAAACGCAAAATTACCGCCGCGCCAGTGGTCGATGAAAACGGCAAACTCACCGGCGCCATTAACCTGCAGGATTTCTACCAGGCGGGGATTATCTAATCCTTCAGTCCCAGACGCTTCGCCAGCCGATGCAGGTTGGCGACGTCGGTTTCCAGCGCCCGCGCGCTGGCCGCCCAGTTATGATTATTTTGCGCCAGCGCCTGGCGAATCATCTCTCGCTGGAAGTTCTCCGTCGATTCGCGCAAATTGCGGCAAGTCGGCAGCGCCAGAAAGCTTTCCGCAGGCGGCGCGGGTAAAACGTCCTCTGACAAGGCAAAATGCTGTGCCTCCAGTATCACCTCATCCCCTGCCCGGGTCGCTCTCGCCAGTACAACCGCACGGTGAATGGCATGTTCCAGCTCCCGGACGTTGCCCGGCCAGCCATAGTTGAGCAAATGGCGACGTGCGCCGGGACTCAGTACCACGCGGGACAGCCCCAGCCGCAGTCGGCACTGCTCGCAAAAATAGCCCGCCAGCAGCACCACATCATCGCCGCGCTCGCGCAGCGGCGGCACAAAGAGCGGGAAAACGCTCAGGCGATGGAACAGATCGGCGCGAAAACGCCCTGCCAGCACCTCTTCACGCAGGTCACGGTTGGTCGCCGCCAACACCCGCACGTCCACGCGCAGGCTACGATCGTCGCCGACGCGCTGAATATCGCCATACTGCAACACGCGAAGTAGCTTAGCCTGTAGCGCCAGCGACAGTTCGCCAATCTCATCCAGAAACAGCGTACCGTTATCCGCCATTTCGAACTTACCGCTACGATTACTGATAGCCCCGGTAAAAGCCCCTTTTACATGACCAAACAACTCGCTCTCCGCCACGCTTTCCGGCAGCGCGGCGCAGTTGAGATAGACCAGCGGATTAACCGCTCTGGGGGAGCCCTGGTGAATAGCTTTCGCCACCAGCTCTTTACCGGTCCCCGTTTCACCGCCGATCAGCACGTTAAGATCGGAGCCCGCCACAATCTCGATCTCTTTTTTCAACTGCGTCATCGCCGGCGACAGGCCGATCATGTGCGTCTCTTTTATCGGTTCAAACACGCCTGACGACCCCGGCAGCATGTTCTGGCTTTCCAGTTGTTCAATTAACAGCGCATTACTCAATGCCCCGGCGGCCAGCGCGGCGACAAGCCGTAGTTCTTCATCGCTAAATACCTCGAACTGCTCCGGCGTCATAGCATCAAGGGTCAGCGCACCGATGAGGTTCTGTCCGGCAAACAGCGGCAGACCAACACAGGCGTGGACTTTCAGGCTTTCCTGTCCGGGAATTAACCCGTCATACGGATCGGGTAAATCGCTATCAGCCGGAAAACGCACCACGTCCCCCGCGCGGGCGATGGCTTCCAGGCGCGGATGCCCTTCCAGGGTAAAACGTCTGCCGAGGACGTCCTGCGCCAGGCCATCAATCGCCAGTGGAATAAATTGTCGTGATTCATAGCGCAGCAGCGCCGAGGCGTCGCACGCCAGCACCTGACGCAGCGTAGTAATCAGCCGCTGAAAACGATCCTGATGCCCAATGCCGCGTTGTAACTCAATGGCGATGCCCGCCAATACCTCCACGGAAAAACTCATGGTTACCTCATTGTCATTTTGACAACCTATAGTGTCATATTGACAGCATCATTTATAGTCTTTTTGACTACATCAAAAATACAAAACAAATATAACTCAATACAAATCAATAAGATGAAAAGTTGGCACACTAGCTGCAATAAGCAAAACAACTTTTTGTAAACGTTGAATGAATTGAGGTGGTTATGTCTATTCTGGTTAAAAATAATATTCATTGGGTTGGCCAGCGCGACTGGGAAGTACGTGATTTTCA"


def GCcontent(DNA):
    """Counts number of occurrences of G's or C's in a DNA string."""
    counter = 0
    for CharacterFromDNA in DNA:
        if CharacterFromDNA == 'G' or CharacterFromDNA == 'C':
            counter = counter + 1
    return counter * 1.0 / (len(DNA))


print(GCcontent('ACCGC'))
print(GCcontent('ATACTAAA'))
print(GCcontent(inIsland))  # GC content of inIsland is 0.4275
print(GCcontent(outsideIsland))  # GC content of outsideIland is 0.5427