import sys, pygame, math, numpy, random, time, copy, operator
from pygame.locals import *

from constants import *
from utils import *
from core import *

def myCreatePathNetwork (OO00OO0OOOO0OO0OO ,O00OO000OO0O00O00 =None ):#line:1
    OOO0000O00O0O0OOO =[]#line:2
    O0OO0OO0O0O0OO00O =[]#line:3
    OO0O0O0OOOO0O0O00 =[]#line:4
    OO0000O0O000OOO0O =[]#line:6
    OO0O0O0OOOO0O0O00 =computePolygons (OO00OO0OOOO0OO0OO )#line:7
    O0O0O000OOO0O0OO0 =[]#line:11
    for OOO00000OO000O0O0 in OO0O0O0OOOO0O0O00 :#line:12
        OOO0000O00O0O0OOO =[]#line:13
        O00O000OO0O00OO0O =None #line:14
        for O0O0O0O00OO0O0O00 in OOO00000OO000O0O0 :#line:15
            if O00O000OO0O00OO0O !=None :#line:16
                O000O0OO00000OOOO =((O00O000OO0O00OO0O [0 ]+O0O0O0O00OO0O0O00 [0 ])/2.0 ,(O00O000OO0O00OO0O [1 ]+O0O0O0O00OO0O0O00 [1 ])/2.0 )#line:18
                O0OOOOO00O00OOOOO =False #line:19
                for O0000OOOO0O000O00 in OO0O0O0OOOO0O0O00 :#line:20
                    for OO000OO00O0O0OOOO in O0000OOOO0O000O00 :#line:21
                        if distance (O000O0OO00000OOOO ,OO000OO00O0O0OOOO )<OO00OO0OOOO0OO0OO .agent .rect .width :#line:22
                            O0OOOOO00O00OOOOO =True #line:23
                if not O0OOOOO00O00OOOOO :#line:24
                    OOO0000O00O0O0OOO .append (O000O0OO00000OOOO )#line:25
            O00O000OO0O00OO0O =O0O0O0O00OO0O0O00 #line:26
        O000O0OO00000OOOO =((OOO00000OO000O0O0 [0 ][0 ]+OOO00000OO000O0O0 [len (OOO00000OO000O0O0 )-1 ][0 ])/2.0 ,(OOO00000OO000O0O0 [0 ][1 ]+OOO00000OO000O0O0 [len (OOO00000OO000O0O0 )-1 ][1 ])/2.0 )#line:28
        O0OOOOO00O00OOOOO =False #line:29
        for O0000OOOO0O000O00 in OO0O0O0OOOO0O0O00 :#line:30
            for OO000OO00O0O0OOOO in O0000OOOO0O000O00 :#line:31
                if distance (O000O0OO00000OOOO ,OO000OO00O0O0OOOO )<OO00OO0OOOO0OO0OO .agent .rect .width :#line:32
                    O0OOOOO00O00OOOOO =True #line:33
        if not O0OOOOO00O00OOOOO :#line:34
            OOO0000O00O0O0OOO .append (O000O0OO00000OOOO )#line:35
        O0O0O000OOO0O0OO0 .append ((OOO00000OO000O0O0 ,OOO0000O00O0O0OOO ))#line:36
    for OO0000OO00OOOOOO0 in O0O0O000OOO0O0OO0 :#line:37
        for OO00O0O00OOO00O00 in OO0000OO00OOOOOO0 [1 ]:#line:38
            for OO00O000OO000OO00 in OO0000OO00OOOOOO0 [1 ]:#line:39
                if OO00O0O00OOO00O00 !=OO00O000OO000OO00 :#line:40
                    OO0O0OOOO0O00O00O =True #line:41
                    for OO000OOOO0O0O00O0 in OO00OO0OOOO0OO0OO .obstacles :#line:42
                        if pointOnPolygon (OO00O0O00OOO00O00 ,OO000OOOO0O0O00O0 .getPoints ())or pointOnPolygon (OO00O000OO000OO00 ,OO000OOOO0O0O00O0 .getPoints ())or pointOnPolygon (OO00O0O00OOO00O00 ,[(0 ,0 ),(SCREEN [0 ],0 ),SCREEN ,(0 ,SCREEN [1 ])])or pointOnPolygon (OO00O000OO000OO00 ,[(0 ,0 ),(SCREEN [0 ],0 ),SCREEN ,(0 ,SCREEN [1 ])]):#line:43
                            OO0O0OOOO0O00O00O =False #line:44
                    if OO0O0OOOO0O00O00O :#line:45
                        OO0O0OOO0O0O0OOOO =(OO00O0O00OOO00O00 ,OO00O000OO000OO00 )#line:46
                        OO0OOOO00OOOO000O =False #line:48
                        for OO00OO0OO00000O00 in O0OO0OO0O0O0OO00O :#line:49
                            if (OO00OO0OO00000O00 [0 ]==OO0O0OOO0O0O0OOOO [0 ]and OO00OO0OO00000O00 [1 ]==OO0O0OOO0O0O0OOOO [1 ])or (OO00OO0OO00000O00 [0 ]==OO0O0OOO0O0O0OOOO [1 ]and OO00OO0OO00000O00 [1 ]==OO0O0OOO0O0O0OOOO [0 ]):#line:50
                                OO0OOOO00OOOO000O =True #line:51
                        if not OO0OOOO00OOOO000O :#line:52
                            O0OOOOO00O00OOOOO =False #line:54
                            for O0O00O0O000O00OOO in OO00OO0OOOO0OO0OO .getPoints ():#line:55
                                if minimumDistance (OO0O0OOO0O0O0OOOO ,O0O00O0O000O00OOO )<OO00OO0OOOO0OO0OO .agent .rect .width :#line:56
                                    O0OOOOO00O00OOOOO =True #line:57
                            if not O0OOOOO00O00OOOOO :#line:58
                                O0OO0OO0O0O0OO00O .append (OO0O0OOO0O0O0OOOO )#line:60
                                OO0000O0O000OOO0O .append (OO00O0O00OOO00O00 )#line:61
                                OO0000O0O000OOO0O .append (OO00O000OO000OO00 )#line:62
    OO0000O0O000OOO0O =list (set (OO0000O0O000OOO0O ))#line:63
    OOO0000O00O0O0OOO =OO0000O0O000OOO0O #line:64
    O0O0O00O0000O0000 ,OOOO0OO000OO0OOO0 =foox (OOO0000O00O0O0OOO ,O0OO0OO0O0O0OO00O )#line:85
    for O0O0O0O00OO0O0O00 in OOO0000O00O0O0OOO :#line:86
        if (map (lambda O0O0OO00OO00OO0O0 :O0O0OO00OO00OO0O0 [0 ],O0OO0OO0O0O0OO00O )+map (lambda O00OOO0OOOO00O00O :O00OOO0OOOO00O00O [1 ],O0OO0OO0O0O0OO00O )).count (O0O0O0O00OO0O0O00 )==1 :#line:87
            OO000O0O0OO0OO0O0 =sorted (OOOO0OO000OO0OOO0 .items (),key =operator .itemgetter (1 ))#line:89
            OO000O0O0OO0OO0O0 .reverse ()#line:90
            for O0O00OO0OOO0000O0 in OO000O0O0OO0OO0O0 :#line:91
                OOOOOOOO000O00OO0 =rayTraceWorld (O0O0O0O00OO0O0O00 ,O0O00OO0OOO0000O0 [0 ],OO00OO0OOOO0OO0OO .getLines ())#line:92
                if OOOOOOOO000O00OO0 ==None :#line:93
                    OO0O0OOO0O0O0OOOO =(O0O0O0O00OO0O0O00 ,O0O00OO0OOO0000O0 [0 ])#line:94
                    O0OOOOO00O00OOOOO =False #line:95
                    for OO000OO00O0O0OOOO in OO00OO0OOOO0OO0OO .getPoints ():#line:96
                        if minimumDistance (OO0O0OOO0O0O0OOOO ,OO000OO00O0O0OOOO )<OO00OO0OOOO0OO0OO .agent .rect .width :#line:97
                            O0OOOOO00O00OOOOO =True #line:98
                            break #line:99
                    if not O0OOOOO00O00OOOOO :#line:100
                        O0OO0OO0O0O0OO00O .append (OO0O0OOO0O0O0OOOO )#line:101
                        break #line:102
    return OOO0000O00O0O0OOO ,O0OO0OO0O0O0OO00O ,OO0O0O0OOOO0O0O00 #line:104
def computePolygons (OOOO0O000O0OO0O00 ):#line:107
    OO0OO0O00000OO00O =[]#line:108
    O00OO00O00OO0O0OO =OOOO0O000O0OO0O00 .getPoints ()#line:109
    OOO0O0OOOOO000000 =OOOO0O000O0OO0O00 .getLines ()#line:110
    corerandom .shuffle (O00OO00O00OO0O0OO )#line:111
    for OOO00O0OOO00O00O0 in O00OO00O00OO0O0OO :#line:112
        for O0OOOOOO0O0OO0000 in O00OO00O00OO0O0OO :#line:113
            if OOO00O0OOO00O00O0 !=O0OOOOOO0O0OO0000 :#line:114
                OO000O00O0OOOO00O =rayTraceWorldNoEndPoints (OOO00O0OOO00O00O0 ,O0OOOOOO0O0OO0000 ,OOO0O0OOOOO000000 )#line:115
                if OO000O00O0OOOO00O ==None :#line:116
                    appendLineNoDuplicates ((OOO00O0OOO00O00O0 ,O0OOOOOO0O0OO0000 ),OOO0O0OOOOO000000 )#line:117
    for OOO00O0OOO00O00O0 in O00OO00O00OO0O0OO :#line:120
        O0OO0OO0OO0OOOO00 =successorPoints (OOO00O0OOO00O00O0 ,OOO0O0OOOOO000000 )#line:121
        for O0OOOOOO0O0OO0000 in O0OO0OO0OO0OOOO00 :#line:122
            OO000OOO000O0O0OO =successorPoints (O0OOOOOO0O0OO0000 ,OOO0O0OOOOO000000 )#line:123
            for OOOOOO0O00OOOO00O in OO000OOO000O0O0OO :#line:124
                OO0OOOOOOO00OO0OO =successorPoints (OOOOOO0O00OOOO00O ,OOO0O0OOOOO000000 )#line:125
                for OO00O00OOO00O00OO in OO0OOOOOOO00OO0OO :#line:126
                    if OO00O00OOO00O00OO ==OOO00O0OOO00O00O0 :#line:127
                        OO0OO0O00000OO00O .append ((OOO00O0OOO00O00O0 ,O0OOOOOO0O0OO0000 ,OOOOOO0O00OOOO00O ))#line:128
    OO0OO0O00000OO00O =map (lambda OOOOO00OOOO00000O :tuple (sorted (OOOOO00OOOO00000O )),OO0OO0O00000OO00O )#line:130
    OO0OO0O00000OO00O =list (set (OO0OO0O00000OO00O ))#line:131
    O0O00O00OO0O00O0O =[]#line:133
    for OOOOO0OO000OOOO0O in OO0OO0O00000OO00O :#line:134
        O00O000O0OOOO0000 =True #line:136
        for O00000000000OO0O0 in OOOO0O000O0OO0O00 .obstacles :#line:137
            if O00O000O0OOOO0000 ==True :#line:138
                if O00000000000OO0O0 .isInPoints (OOOOO0OO000OOOO0O [0 ])and O00000000000OO0O0 .isInPoints (OOOOO0OO000OOOO0O [1 ])and O00000000000OO0O0 .isInPoints (OOOOO0OO000OOOO0O [2 ]):#line:139
                    if pointInsidePolygonPoints ((sum (map (lambda OO00OOO0000OO000O :OO00OOO0000OO000O [0 ],OOOOO0OO000OOOO0O ))/3.0 ,sum (map (lambda OO0OOOOO0O0000OO0 :OO0OOOOO0O0000OO0 [1 ],OOOOO0OO000OOOO0O ))/3.0 ),O00000000000OO0O0 .getPoints ()):#line:140
                        O00O000O0OOOO0000 =False #line:141
        if O00O000O0OOOO0000 ==True :#line:148
            O0O00O00OO0O00O0O .append (OOOOO0OO000OOOO0O )#line:149
    O00O0000O0OOO000O =[]#line:150
    for OO0OO00O0O00OOO00 in O0O00O00OO0O00O0O :#line:152
        O00O000O0OOOO0000 =True #line:153
        for OOOOO0O00OOOOO0O0 in O0O00O00OO0O00O0O :#line:154
            if OO0OO00O0O00OOO00 !=OOOOO0O00OOOOO0O0 and O00O000O0OOOO0000 ==True :#line:155
                O0OOOOOO0O0OO000O =list (set (OOOOO0O00OOOOO0O0 )-set (OO0OO00O0O00OOO00 ))#line:156
                if len (O0OOOOOO0O0OO000O )==1 :#line:157
                    OO0OOO00O0O0O0OOO =O0OOOOOO0O0OO000O [0 ]#line:158
                    if pointInsidePolygonPoints (OO0OOO00O0O0O0OOO ,OO0OO00O0O00OOO00 ):#line:159
                        O00O000O0OOOO0000 =False #line:160
        if O00O000O0OOOO0000 :#line:161
            O00O0000O0OOO000O .append (OO0OO00O0O00OOO00 )#line:162
    OOOOO0OOOO0000OOO =O00O0000O0OOO000O #line:167
    OOOOO0O000O00O00O =[]#line:170
    O0OO0O0O00O000OOO =[]#line:171
    for OOO00OO0O0O0O0O00 in OOOOO0OOOO0000OOO :#line:172
        for O0O0OO0OOOO00O000 in OOOOO0OOOO0000OOO :#line:173
            if OOO00OO0O0O0O0O00 !=O0O0OO0OOOO00O000 and O0O0OO0OOOO00O000 not in O0OO0O0O00O000OOO and OOO00OO0O0O0O0O00 not in O0OO0O0O00O000OOO :#line:174
                if polygonsAdjacent (OOO00OO0O0O0O0O00 ,O0O0OO0OOOO00O000 ):#line:175
                    O0OOOO0O0O000OOO0 =tuple (set (list (OOO00OO0O0O0O0O00 )+list (O0O0OO0OOOO00O000 )))#line:176
                    if isConvex (O0OOOO0O0O000OOO0 ):#line:177
                        OOOOO0O000O00O00O .append (O0OOOO0O0O000OOO0 )#line:178
                        O0OO0O0O00O000OOO .append (OOO00OO0O0O0O0O00 )#line:179
                        O0OO0O0O00O000OOO .append (O0O0OO0OOOO00O000 )#line:180
                        break #line:181
    OOOOO0OOOO0000OOO =OOOOO0O000O00O00O +list (set (OOOOO0OOOO0000OOO )-set (O0OO0O0O00O000OOO ))#line:182
    return OOOOO0OOOO0000OOO #line:183
def polygonsOverlap (O0O0OOO0000O0OO00 ,O0OO000O00O00OO0O ):#line:197
    OO000OOOOOOO0OO0O =[]#line:198
    O0OO0000O0000O0O0 =[]#line:200
    OOO0O0O00000O0OOO =None #line:201
    for O00O0000OO0000O0O in O0O0OOO0000O0OO00 :#line:202
        if OOO0O0O00000O0OOO !=None :#line:203
            O0OO0000O0000O0O0 .append ((OOO0O0O00000O0OOO ,O00O0000OO0000O0O ))#line:204
        OOO0O0O00000O0OOO =O00O0000OO0000O0O #line:205
    O0OO0000O0000O0O0 .append ((O0O0OOO0000O0OO00 [0 ],O0O0OOO0000O0OO00 [len (O0O0OOO0000O0OO00 )-1 ]))#line:206
    O0OOO00O000OO0O00 =[]#line:208
    OOO0O0O00000O0OOO =None #line:209
    for O00O0000OO0000O0O in O0OO000O00O00OO0O :#line:210
        if OOO0O0O00000O0OOO !=None :#line:211
            O0OOO00O000OO0O00 .append ((OOO0O0O00000O0OOO ,O00O0000OO0000O0O ))#line:212
        OOO0O0O00000O0OOO =O00O0000OO0000O0O #line:213
    O0OOO00O000OO0O00 .append ((O0OO000O00O00OO0O [0 ],O0OO000O00O00OO0O [len (O0OO000O00O00OO0O )-1 ]))#line:214
    for O0OO00OO0O0OOOOOO in O0OO0000O0000O0O0 :#line:216
        O000O0OOOOOOOO0O0 =(sum (map (lambda OO0000000O00OO0OO :OO0000000O00OO0OO [0 ],O0OO00OO0O0OOOOOO ))/2.0 ,sum (map (lambda O0O00000000O0OO00 :O0O00000000O0OO00 [1 ],O0OO00OO0O0OOOOOO ))/2.0 )#line:217
        if pointInsidePolygon (O000O0OOOOOOOO0O0 ,O0OOO00O000OO0O00 ):#line:218
            OO000OOOOOOO0OO0O .append (O0OO00OO0O0OOOOOO [0 ])#line:219
            OO000OOOOOOO0OO0O .append (O0OO00OO0O0OOOOOO [1 ])#line:220
    if len (OO000OOOOOOO0OO0O )>0 :#line:221
        return OO000OOOOOOO0OO0O #line:222
    else :#line:223
        return False #line:224
def successorPoints (O0000000OO0O00OO0 ,O0O0OOO00OOOOOO00 ):#line:229
    OOOO0O00OO0OOO00O =set ()#line:230
    for OO0O00OOOO0OO0000 in O0O0OOO00OOOOOO00 :#line:231
        if (OO0O00OOOO0OO0000 [0 ]==O0000000OO0O00OO0 ):#line:232
            OOOO0O00OO0OOO00O .add (OO0O00OOOO0OO0000 [1 ])#line:233
        elif (OO0O00OOOO0OO0000 [1 ]==O0000000OO0O00OO0 ):#line:234
            OOOO0O00OO0OOO00O .add (OO0O00OOOO0OO0000 [0 ])#line:235
    return list (OOOO0O00OO0OOO00O )#line:236
def foox (O00O0OOOO0OOO0OOO ,O00O000OO00000OOO ):#line:242
    OO0O00000000O0000 ={}#line:243
    OOO0OO0000O00OOO0 ={}#line:244
    for OO0O0OOO0000O0O00 in O00O0OOOO0OOO0OOO :#line:245
        OOO0OO0000O00OOO0 [OO0O0OOO0000O0O00 ]={}#line:246
        OO0O00000000O0000 [OO0O0OOO0000O0O00 ]={}#line:247
    for OOOOOOOOO000000OO in O00O0OOOO0OOO0OOO :#line:249
        for O0OO00OO0OOO0000O in O00O0OOOO0OOO0OOO :#line:250
            OOO0OO0000O00OOO0 [OOOOOOOOO000000OO ][O0OO00OO0OOO0000O ]=None #line:251
            OOO0OO0000O00OOO0 [O0OO00OO0OOO0000O ][OOOOOOOOO000000OO ]=None #line:252
            if OOOOOOOOO000000OO ==O0OO00OO0OOO0000O :#line:253
                OO0O00000000O0000 [OOOOOOOOO000000OO ][O0OO00OO0OOO0000O ]=0 #line:254
                OO0O00000000O0000 [O0OO00OO0OOO0000O ][OOOOOOOOO000000OO ]=0 #line:255
            else :#line:256
                OO0O00000000O0000 [OOOOOOOOO000000OO ][O0OO00OO0OOO0000O ]=INFINITY #line:257
                OO0O00000000O0000 [O0OO00OO0OOO0000O ][OOOOOOOOO000000OO ]=INFINITY #line:258
    OOOO000O0OO0O0OO0 =INFINITY #line:259
    for OO0O0OO0O0OOO0OOO in O00O000OO00000OOO :#line:260
        OOOO000O0OO0O0OO0 =distance (OO0O0OO0O0OOO0OOO [0 ],OO0O0OO0O0OOO0OOO [1 ])#line:261
        OO0O00000000O0000 [OO0O0OO0O0OOO0OOO [0 ]][OO0O0OO0O0OOO0OOO [1 ]]=OOOO000O0OO0O0OO0 #line:262
        OO0O00000000O0000 [OO0O0OO0O0OOO0OOO [1 ]][OO0O0OO0O0OOO0OOO [0 ]]=OOOO000O0OO0O0OO0 #line:263
    for OO0O0000OO00OO000 in O00O0OOOO0OOO0OOO :#line:264
        for O000O0O00000OOOO0 in O00O0OOOO0OOO0OOO :#line:265
            for O000OO00O00OO0000 in O00O0OOOO0OOO0OOO :#line:266
                if OO0O00000000O0000 [O000O0O00000OOOO0 ][OO0O0000OO00OO000 ]+OO0O00000000O0000 [OO0O0000OO00OO000 ][O000OO00O00OO0000 ]<OO0O00000000O0000 [O000O0O00000OOOO0 ][O000OO00O00OO0000 ]:#line:267
                    OO0O00000000O0000 [O000O0O00000OOOO0 ][O000OO00O00OO0000 ]=OO0O00000000O0000 [O000O0O00000OOOO0 ][OO0O0000OO00OO000 ]+OO0O00000000O0000 [OO0O0000OO00OO000 ][O000OO00O00OO0000 ]#line:268
                    OOO0OO0000O00OOO0 [O000O0O00000OOOO0 ][O000OO00O00OO0000 ]=OO0O0000OO00OO000 #line:269
    return OOO0OO0000O00OOO0 ,OO0O00000000O0000
#e9015584e6a44b14988f13e2298bcbf9


#===============================================================#
# Obfuscated by Oxyry Python Obfuscator (http://pyob.oxyry.com) #
#===============================================================#
