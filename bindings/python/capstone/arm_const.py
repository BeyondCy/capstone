# For Capstone Engine. AUTO-GENERATED FILE, DO NOT EDIT [arm_const.py]

# ARM shift type

ARM_SFT_INVALID = 0
ARM_SFT_ASR = 1
ARM_SFT_LSL = 2
ARM_SFT_LSR = 3
ARM_SFT_ROR = 4
ARM_SFT_RRX = 5
ARM_SFT_ASR_REG = 6
ARM_SFT_LSL_REG = 7
ARM_SFT_LSR_REG = 8
ARM_SFT_ROR_REG = 9
ARM_SFT_RRX_REG = 10

# ARM condition code

ARM_CC_INVALID = 0
ARM_CC_EQ = 1
ARM_CC_NE = 2
ARM_CC_HS = 3
ARM_CC_LO = 4
ARM_CC_MI = 5
ARM_CC_PL = 6
ARM_CC_VS = 7
ARM_CC_VC = 8
ARM_CC_HI = 9
ARM_CC_LS = 10
ARM_CC_GE = 11
ARM_CC_LT = 12
ARM_CC_GT = 13
ARM_CC_LE = 14
ARM_CC_AL = 15

# Operand type for instruction's operands

ARM_OP_INVALID = 0
ARM_OP_REG = 1
ARM_OP_CIMM = 2
ARM_OP_PIMM = 3
ARM_OP_IMM = 4
ARM_OP_FP = 5
ARM_OP_MEM = 6

# ARM registers

ARM_REG_INVALID = 0
ARM_REG_APSR = 1
ARM_REG_APSR_NZCV = 2
ARM_REG_CPSR = 3
ARM_REG_FPEXC = 4
ARM_REG_FPINST = 5
ARM_REG_FPSCR = 6
ARM_REG_FPSCR_NZCV = 7
ARM_REG_FPSID = 8
ARM_REG_ITSTATE = 9
ARM_REG_LR = 10
ARM_REG_PC = 11
ARM_REG_SP = 12
ARM_REG_SPSR = 13
ARM_REG_D0 = 14
ARM_REG_D1 = 15
ARM_REG_D2 = 16
ARM_REG_D3 = 17
ARM_REG_D4 = 18
ARM_REG_D5 = 19
ARM_REG_D6 = 20
ARM_REG_D7 = 21
ARM_REG_D8 = 22
ARM_REG_D9 = 23
ARM_REG_D10 = 24
ARM_REG_D11 = 25
ARM_REG_D12 = 26
ARM_REG_D13 = 27
ARM_REG_D14 = 28
ARM_REG_D15 = 29
ARM_REG_D16 = 30
ARM_REG_D17 = 31
ARM_REG_D18 = 32
ARM_REG_D19 = 33
ARM_REG_D20 = 34
ARM_REG_D21 = 35
ARM_REG_D22 = 36
ARM_REG_D23 = 37
ARM_REG_D24 = 38
ARM_REG_D25 = 39
ARM_REG_D26 = 40
ARM_REG_D27 = 41
ARM_REG_D28 = 42
ARM_REG_D29 = 43
ARM_REG_D30 = 44
ARM_REG_D31 = 45
ARM_REG_FPINST2 = 46
ARM_REG_MVFR0 = 47
ARM_REG_MVFR1 = 48
ARM_REG_MVFR2 = 49
ARM_REG_Q0 = 50
ARM_REG_Q1 = 51
ARM_REG_Q2 = 52
ARM_REG_Q3 = 53
ARM_REG_Q4 = 54
ARM_REG_Q5 = 55
ARM_REG_Q6 = 56
ARM_REG_Q7 = 57
ARM_REG_Q8 = 58
ARM_REG_Q9 = 59
ARM_REG_Q10 = 60
ARM_REG_Q11 = 61
ARM_REG_Q12 = 62
ARM_REG_Q13 = 63
ARM_REG_Q14 = 64
ARM_REG_Q15 = 65
ARM_REG_R0 = 66
ARM_REG_R1 = 67
ARM_REG_R2 = 68
ARM_REG_R3 = 69
ARM_REG_R4 = 70
ARM_REG_R5 = 71
ARM_REG_R6 = 72
ARM_REG_R7 = 73
ARM_REG_R8 = 74
ARM_REG_R9 = 75
ARM_REG_R10 = 76
ARM_REG_R11 = 77
ARM_REG_R12 = 78
ARM_REG_S0 = 79
ARM_REG_S1 = 80
ARM_REG_S2 = 81
ARM_REG_S3 = 82
ARM_REG_S4 = 83
ARM_REG_S5 = 84
ARM_REG_S6 = 85
ARM_REG_S7 = 86
ARM_REG_S8 = 87
ARM_REG_S9 = 88
ARM_REG_S10 = 89
ARM_REG_S11 = 90
ARM_REG_S12 = 91
ARM_REG_S13 = 92
ARM_REG_S14 = 93
ARM_REG_S15 = 94
ARM_REG_S16 = 95
ARM_REG_S17 = 96
ARM_REG_S18 = 97
ARM_REG_S19 = 98
ARM_REG_S20 = 99
ARM_REG_S21 = 100
ARM_REG_S22 = 101
ARM_REG_S23 = 102
ARM_REG_S24 = 103
ARM_REG_S25 = 104
ARM_REG_S26 = 105
ARM_REG_S27 = 106
ARM_REG_S28 = 107
ARM_REG_S29 = 108
ARM_REG_S30 = 109
ARM_REG_S31 = 110
ARM_REG_MAX = 111
ARM_REG_R13 = ARM_REG_SP
ARM_REG_R14 = ARM_REG_LR
ARM_REG_R15 = ARM_REG_PC

# ARM instruction

ARM_INS_INVALID = 0
ARM_INS_ADC = 1
ARM_INS_ADD = 2
ARM_INS_ADR = 3
ARM_INS_AESD = 4
ARM_INS_AESE = 5
ARM_INS_AESIMC = 6
ARM_INS_AESMC = 7
ARM_INS_AND = 8
ARM_INS_BFC = 9
ARM_INS_BFI = 10
ARM_INS_BIC = 11
ARM_INS_BKPT = 12
ARM_INS_BL = 13
ARM_INS_BLX = 14
ARM_INS_BX = 15
ARM_INS_BXJ = 16
ARM_INS_B = 17
ARM_INS_CDP = 18
ARM_INS_CDP2 = 19
ARM_INS_CLREX = 20
ARM_INS_CLZ = 21
ARM_INS_CMN = 22
ARM_INS_CMP = 23
ARM_INS_CPS = 24
ARM_INS_CRC32B = 25
ARM_INS_CRC32CB = 26
ARM_INS_CRC32CH = 27
ARM_INS_CRC32CW = 28
ARM_INS_CRC32H = 29
ARM_INS_CRC32W = 30
ARM_INS_DBG = 31
ARM_INS_DMB = 32
ARM_INS_DSB = 33
ARM_INS_EOR = 34
ARM_INS_VMOV = 35
ARM_INS_FLDMDBX = 36
ARM_INS_FLDMIAX = 37
ARM_INS_VMRS = 38
ARM_INS_FSTMDBX = 39
ARM_INS_FSTMIAX = 40
ARM_INS_HINT = 41
ARM_INS_HLT = 42
ARM_INS_ISB = 43
ARM_INS_LDA = 44
ARM_INS_LDAB = 45
ARM_INS_LDAEX = 46
ARM_INS_LDAEXB = 47
ARM_INS_LDAEXD = 48
ARM_INS_LDAEXH = 49
ARM_INS_LDAH = 50
ARM_INS_LDC2L = 51
ARM_INS_LDC2 = 52
ARM_INS_LDCL = 53
ARM_INS_LDC = 54
ARM_INS_LDMDA = 55
ARM_INS_LDMDB = 56
ARM_INS_LDM = 57
ARM_INS_LDMIB = 58
ARM_INS_LDRBT = 59
ARM_INS_LDRB = 60
ARM_INS_LDRD = 61
ARM_INS_LDREX = 62
ARM_INS_LDREXB = 63
ARM_INS_LDREXD = 64
ARM_INS_LDREXH = 65
ARM_INS_LDRH = 66
ARM_INS_LDRHT = 67
ARM_INS_LDRSB = 68
ARM_INS_LDRSBT = 69
ARM_INS_LDRSH = 70
ARM_INS_LDRSHT = 71
ARM_INS_LDRT = 72
ARM_INS_LDR = 73
ARM_INS_MCR = 74
ARM_INS_MCR2 = 75
ARM_INS_MCRR = 76
ARM_INS_MCRR2 = 77
ARM_INS_MLA = 78
ARM_INS_MLS = 79
ARM_INS_MOV = 80
ARM_INS_MOVT = 81
ARM_INS_MOVW = 82
ARM_INS_MRC = 83
ARM_INS_MRC2 = 84
ARM_INS_MRRC = 85
ARM_INS_MRRC2 = 86
ARM_INS_MRS = 87
ARM_INS_MSR = 88
ARM_INS_MUL = 89
ARM_INS_MVN = 90
ARM_INS_ORR = 91
ARM_INS_PKHBT = 92
ARM_INS_PKHTB = 93
ARM_INS_PLDW = 94
ARM_INS_PLD = 95
ARM_INS_PLI = 96
ARM_INS_QADD = 97
ARM_INS_QADD16 = 98
ARM_INS_QADD8 = 99
ARM_INS_QASX = 100
ARM_INS_QDADD = 101
ARM_INS_QDSUB = 102
ARM_INS_QSAX = 103
ARM_INS_QSUB = 104
ARM_INS_QSUB16 = 105
ARM_INS_QSUB8 = 106
ARM_INS_RBIT = 107
ARM_INS_REV = 108
ARM_INS_REV16 = 109
ARM_INS_REVSH = 110
ARM_INS_RFEDA = 111
ARM_INS_RFEDB = 112
ARM_INS_RFEIA = 113
ARM_INS_RFEIB = 114
ARM_INS_RSB = 115
ARM_INS_RSC = 116
ARM_INS_SADD16 = 117
ARM_INS_SADD8 = 118
ARM_INS_SASX = 119
ARM_INS_SBC = 120
ARM_INS_SBFX = 121
ARM_INS_SDIV = 122
ARM_INS_SEL = 123
ARM_INS_SETEND = 124
ARM_INS_SHA1C = 125
ARM_INS_SHA1H = 126
ARM_INS_SHA1M = 127
ARM_INS_SHA1P = 128
ARM_INS_SHA1SU0 = 129
ARM_INS_SHA1SU1 = 130
ARM_INS_SHA256H = 131
ARM_INS_SHA256H2 = 132
ARM_INS_SHA256SU0 = 133
ARM_INS_SHA256SU1 = 134
ARM_INS_SHADD16 = 135
ARM_INS_SHADD8 = 136
ARM_INS_SHASX = 137
ARM_INS_SHSAX = 138
ARM_INS_SHSUB16 = 139
ARM_INS_SHSUB8 = 140
ARM_INS_SMC = 141
ARM_INS_SMLABB = 142
ARM_INS_SMLABT = 143
ARM_INS_SMLAD = 144
ARM_INS_SMLADX = 145
ARM_INS_SMLAL = 146
ARM_INS_SMLALBB = 147
ARM_INS_SMLALBT = 148
ARM_INS_SMLALD = 149
ARM_INS_SMLALDX = 150
ARM_INS_SMLALTB = 151
ARM_INS_SMLALTT = 152
ARM_INS_SMLATB = 153
ARM_INS_SMLATT = 154
ARM_INS_SMLAWB = 155
ARM_INS_SMLAWT = 156
ARM_INS_SMLSD = 157
ARM_INS_SMLSDX = 158
ARM_INS_SMLSLD = 159
ARM_INS_SMLSLDX = 160
ARM_INS_SMMLA = 161
ARM_INS_SMMLAR = 162
ARM_INS_SMMLS = 163
ARM_INS_SMMLSR = 164
ARM_INS_SMMUL = 165
ARM_INS_SMMULR = 166
ARM_INS_SMUAD = 167
ARM_INS_SMUADX = 168
ARM_INS_SMULBB = 169
ARM_INS_SMULBT = 170
ARM_INS_SMULL = 171
ARM_INS_SMULTB = 172
ARM_INS_SMULTT = 173
ARM_INS_SMULWB = 174
ARM_INS_SMULWT = 175
ARM_INS_SMUSD = 176
ARM_INS_SMUSDX = 177
ARM_INS_SRSDA = 178
ARM_INS_SRSDB = 179
ARM_INS_SRSIA = 180
ARM_INS_SRSIB = 181
ARM_INS_SSAT = 182
ARM_INS_SSAT16 = 183
ARM_INS_SSAX = 184
ARM_INS_SSUB16 = 185
ARM_INS_SSUB8 = 186
ARM_INS_STC2L = 187
ARM_INS_STC2 = 188
ARM_INS_STCL = 189
ARM_INS_STC = 190
ARM_INS_STL = 191
ARM_INS_STLB = 192
ARM_INS_STLEX = 193
ARM_INS_STLEXB = 194
ARM_INS_STLEXD = 195
ARM_INS_STLEXH = 196
ARM_INS_STLH = 197
ARM_INS_STMDA = 198
ARM_INS_STMDB = 199
ARM_INS_STM = 200
ARM_INS_STMIB = 201
ARM_INS_STRBT = 202
ARM_INS_STRB = 203
ARM_INS_STRD = 204
ARM_INS_STREX = 205
ARM_INS_STREXB = 206
ARM_INS_STREXD = 207
ARM_INS_STREXH = 208
ARM_INS_STRH = 209
ARM_INS_STRHT = 210
ARM_INS_STRT = 211
ARM_INS_STR = 212
ARM_INS_SUB = 213
ARM_INS_SVC = 214
ARM_INS_SWP = 215
ARM_INS_SWPB = 216
ARM_INS_SXTAB = 217
ARM_INS_SXTAB16 = 218
ARM_INS_SXTAH = 219
ARM_INS_SXTB = 220
ARM_INS_SXTB16 = 221
ARM_INS_SXTH = 222
ARM_INS_TEQ = 223
ARM_INS_TRAP = 224
ARM_INS_TST = 225
ARM_INS_UADD16 = 226
ARM_INS_UADD8 = 227
ARM_INS_UASX = 228
ARM_INS_UBFX = 229
ARM_INS_UDIV = 230
ARM_INS_UHADD16 = 231
ARM_INS_UHADD8 = 232
ARM_INS_UHASX = 233
ARM_INS_UHSAX = 234
ARM_INS_UHSUB16 = 235
ARM_INS_UHSUB8 = 236
ARM_INS_UMAAL = 237
ARM_INS_UMLAL = 238
ARM_INS_UMULL = 239
ARM_INS_UQADD16 = 240
ARM_INS_UQADD8 = 241
ARM_INS_UQASX = 242
ARM_INS_UQSAX = 243
ARM_INS_UQSUB16 = 244
ARM_INS_UQSUB8 = 245
ARM_INS_USAD8 = 246
ARM_INS_USADA8 = 247
ARM_INS_USAT = 248
ARM_INS_USAT16 = 249
ARM_INS_USAX = 250
ARM_INS_USUB16 = 251
ARM_INS_USUB8 = 252
ARM_INS_UXTAB = 253
ARM_INS_UXTAB16 = 254
ARM_INS_UXTAH = 255
ARM_INS_UXTB = 256
ARM_INS_UXTB16 = 257
ARM_INS_UXTH = 258
ARM_INS_VABAL = 259
ARM_INS_VABA = 260
ARM_INS_VABDL = 261
ARM_INS_VABD = 262
ARM_INS_VABS = 263
ARM_INS_VACGE = 264
ARM_INS_VACGT = 265
ARM_INS_VADD = 266
ARM_INS_VADDHN = 267
ARM_INS_VADDL = 268
ARM_INS_VADDW = 269
ARM_INS_VAND = 270
ARM_INS_VBIC = 271
ARM_INS_VBIF = 272
ARM_INS_VBIT = 273
ARM_INS_VBSL = 274
ARM_INS_VCEQ = 275
ARM_INS_VCGE = 276
ARM_INS_VCGT = 277
ARM_INS_VCLS = 278
ARM_INS_VCLZ = 279
ARM_INS_VCMP = 280
ARM_INS_VCMPE = 281
ARM_INS_VCNT = 282
ARM_INS_VCVTA = 283
ARM_INS_VCVTB = 284
ARM_INS_VCVT = 285
ARM_INS_VCVTM = 286
ARM_INS_VCVTN = 287
ARM_INS_VCVTP = 288
ARM_INS_VCVTT = 289
ARM_INS_VDIV = 290
ARM_INS_VDUP = 291
ARM_INS_VEOR = 292
ARM_INS_VEXT = 293
ARM_INS_VFMA = 294
ARM_INS_VFMS = 295
ARM_INS_VFNMA = 296
ARM_INS_VFNMS = 297
ARM_INS_VHADD = 298
ARM_INS_VHSUB = 299
ARM_INS_VLD1 = 300
ARM_INS_VLD2 = 301
ARM_INS_VLD3 = 302
ARM_INS_VLD4 = 303
ARM_INS_VLDMDB = 304
ARM_INS_VLDMIA = 305
ARM_INS_VLDR = 306
ARM_INS_VMAXNM = 307
ARM_INS_VMAX = 308
ARM_INS_VMINNM = 309
ARM_INS_VMIN = 310
ARM_INS_VMLA = 311
ARM_INS_VMLAL = 312
ARM_INS_VMLS = 313
ARM_INS_VMLSL = 314
ARM_INS_VMOVL = 315
ARM_INS_VMOVN = 316
ARM_INS_VMSR = 317
ARM_INS_VMUL = 318
ARM_INS_VMULL = 319
ARM_INS_VMVN = 320
ARM_INS_VNEG = 321
ARM_INS_VNMLA = 322
ARM_INS_VNMLS = 323
ARM_INS_VNMUL = 324
ARM_INS_VORN = 325
ARM_INS_VORR = 326
ARM_INS_VPADAL = 327
ARM_INS_VPADDL = 328
ARM_INS_VPADD = 329
ARM_INS_VPMAX = 330
ARM_INS_VPMIN = 331
ARM_INS_VQABS = 332
ARM_INS_VQADD = 333
ARM_INS_VQDMLAL = 334
ARM_INS_VQDMLSL = 335
ARM_INS_VQDMULH = 336
ARM_INS_VQDMULL = 337
ARM_INS_VQMOVUN = 338
ARM_INS_VQMOVN = 339
ARM_INS_VQNEG = 340
ARM_INS_VQRDMULH = 341
ARM_INS_VQRSHL = 342
ARM_INS_VQRSHRN = 343
ARM_INS_VQRSHRUN = 344
ARM_INS_VQSHL = 345
ARM_INS_VQSHLU = 346
ARM_INS_VQSHRN = 347
ARM_INS_VQSHRUN = 348
ARM_INS_VQSUB = 349
ARM_INS_VRADDHN = 350
ARM_INS_VRECPE = 351
ARM_INS_VRECPS = 352
ARM_INS_VREV16 = 353
ARM_INS_VREV32 = 354
ARM_INS_VREV64 = 355
ARM_INS_VRHADD = 356
ARM_INS_VRINTA = 357
ARM_INS_VRINTM = 358
ARM_INS_VRINTN = 359
ARM_INS_VRINTP = 360
ARM_INS_VRINTR = 361
ARM_INS_VRINTX = 362
ARM_INS_VRINTZ = 363
ARM_INS_VRSHL = 364
ARM_INS_VRSHRN = 365
ARM_INS_VRSHR = 366
ARM_INS_VRSQRTE = 367
ARM_INS_VRSQRTS = 368
ARM_INS_VRSRA = 369
ARM_INS_VRSUBHN = 370
ARM_INS_VSELEQ = 371
ARM_INS_VSELGE = 372
ARM_INS_VSELGT = 373
ARM_INS_VSELVS = 374
ARM_INS_VSHLL = 375
ARM_INS_VSHL = 376
ARM_INS_VSHRN = 377
ARM_INS_VSHR = 378
ARM_INS_VSLI = 379
ARM_INS_VSQRT = 380
ARM_INS_VSRA = 381
ARM_INS_VSRI = 382
ARM_INS_VST1 = 383
ARM_INS_VST2 = 384
ARM_INS_VST3 = 385
ARM_INS_VST4 = 386
ARM_INS_VSTMDB = 387
ARM_INS_VSTMIA = 388
ARM_INS_VSTR = 389
ARM_INS_VSUB = 390
ARM_INS_VSUBHN = 391
ARM_INS_VSUBL = 392
ARM_INS_VSUBW = 393
ARM_INS_VSWP = 394
ARM_INS_VTBL = 395
ARM_INS_VTBX = 396
ARM_INS_VCVTR = 397
ARM_INS_VTRN = 398
ARM_INS_VTST = 399
ARM_INS_VUZP = 400
ARM_INS_VZIP = 401
ARM_INS_ADDW = 402
ARM_INS_ASR = 403
ARM_INS_DCPS1 = 404
ARM_INS_DCPS2 = 405
ARM_INS_DCPS3 = 406
ARM_INS_IT = 407
ARM_INS_LSL = 408
ARM_INS_LSR = 409
ARM_INS_ORN = 410
ARM_INS_ROR = 411
ARM_INS_RRX = 412
ARM_INS_SUBS = 413
ARM_INS_SUBW = 414
ARM_INS_TBB = 415
ARM_INS_TBH = 416
ARM_INS_CBNZ = 417
ARM_INS_CBZ = 418
ARM_INS_MOVS = 419
ARM_INS_POP = 420
ARM_INS_PUSH = 421
ARM_INS_MAX = 422

# Group of ARM instructions

ARM_GRP_INVALID = 0
ARM_GRP_CRYPTO = 1
ARM_GRP_DATABARRIER = 2
ARM_GRP_DIVIDE = 3
ARM_GRP_FPARMV8 = 4
ARM_GRP_MULTPRO = 5
ARM_GRP_NEON = 6
ARM_GRP_T2EXTRACTPACK = 7
ARM_GRP_THUMB2DSP = 8
ARM_GRP_TRUSTZONE = 9
ARM_GRP_V4T = 10
ARM_GRP_V5T = 11
ARM_GRP_V5TE = 12
ARM_GRP_V6 = 13
ARM_GRP_V6T2 = 14
ARM_GRP_V7 = 15
ARM_GRP_V8 = 16
ARM_GRP_VFP2 = 17
ARM_GRP_VFP3 = 18
ARM_GRP_VFP4 = 19
ARM_GRP_ARM = 20
ARM_GRP_MCLASS = 21
ARM_GRP_NOTMCLASS = 22
ARM_GRP_THUMB = 23
ARM_GRP_THUMB1ONLY = 24
ARM_GRP_THUMB2 = 25
ARM_GRP_PREV8 = 26
ARM_GRP_FPVMLX = 27
ARM_GRP_MULOPS = 28
ARM_GRP_CRC = 29
ARM_GRP_DPVFP = 30
ARM_GRP_V6M = 31
ARM_GRP_JUMP = 32
ARM_GRP_MAX = 33
