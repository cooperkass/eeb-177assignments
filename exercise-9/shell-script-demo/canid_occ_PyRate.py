#!/usr/bin/env python
from numpy import * 


data_1=[array([13.617004,15.312035,13.855598,8.80243,15.740042,12.504051,15.752131,14.940043,15.291375,14.623311,14.902271,8.566597,12.140478]),
array([16.73735,19.573122,14.593065,14.993053,14.786973,15.474544,13.71477,15.241501,14.796293,14.572683,14.413391]),
array([14.497659,16.345985,14.472154,14.874636,12.281962,13.195094,13.967004,13.773657,13.766304,14.417659,13.497301,11.827224,14.972167,13.721027,15.816158,13.2654,18.535242,14.982617,15.234604,14.166252,12.543141,12.067512,13.662326,10.436231,13.662184,14.287547,10.390264,13.195,13.706394,14.115001,14.912006,18.666386,15.855228,15.684477,15.904735,14.158423,14.404267,15.126826,14.887686,15.890415,15.371107,9.579492,15.45943,10.519294,12.877153,13.511078,14.249921,15.031819,6.772727,16.168862,15.341251]),
array([14.886596,15.675731,15.282477,6.571148,14.861869,15.940362,14.490654,15.587521,14.235948]),
array([14.674656]),
array([10.670483,14.368987,10.662375,11.283856,10.520537,11.777718,11.049916,15.930979,14.803466]),
array([10.529339,12.565396,13.22954,10.548636,10.171271,11.615649,11.930723,16.99637,13.441346,11.149473,13.425465,13.495867,11.822851,5.669049,12.243347,12.103603,7.6873,12.745593,6.986977,13.47009,14.530849,10.970119,13.481953,11.64587,12.841492,12.790761,10.847196,10.849765,12.232961,10.687898,12.388577,8.408288,12.685646,11.036511,12.715898,13.128291,13.332969,10.330757,8.451967,11.80621,13.371979,10.499656,13.263183,12.492599,8.802481,12.206899,11.364511,12.319386,13.510344,12.68151,13.264845,10.651198,11.963145,6.788272,10.539216,22.836124,10.785315,11.994856,11.720132,11.544429,11.587308,12.578396]),
array([16.385843]),
array([3.543073]),
array([0.809872,1.578207,0.029494,0.080719,0.029986,0.082343,0.00764,0.07465,0.009019,0.011014,0.01005]),
array([24.155719]),
array([32.310435,32.776857,23.419999,27.384006,23.813974,28.109686,29.250778,23.516877,25.78508,21.290447,20.494012,22.88692,28.235392,29.443552,29.676697,28.513343,28.508798,26.533657,28.515684,27.065296,27.694583,29.780866,28.846788,29.777467,25.22672,22.381303,27.407373]),
array([33.02593,31.213395,30.90352,32.910958,31.029213,31.266456,31.496524,30.192904,28.322586]),
array([20.482228,23.671773,21.272056,19.719338,16.515047,15.6276,15.350911,14.086029,12.961835,13.482661,15.898919,11.641796,15.836687,13.30992,14.852523,10.93162,10.407126,12.180516,5.809291,11.235594,22.103132,15.56723,15.660156,11.501602,16.801538,13.823341,22.689501,10.207079,20.370311,11.639917,5.027603,10.647617,12.020768,17.609448,17.320152,18.893023,5.390097,16.900686,16.343779,17.521907,19.329002,17.015303,18.578607,16.722864,5.364262,15.12371,13.739751,12.599219,11.064803,11.728947,11.093792,10.666949,12.242217,11.017694,15.947037,14.257222,14.008527,16.617433]),
array([7.978061,7.857212,7.507375,7.676797,10.047954,7.708726,7.779258,7.567522,2.398202,6.018715,4.979299,5.263499,8.95257,5.267342,17.893784,10.286223,7.363977,10.285019,5.205772,6.742403,7.955006,5.085603,3.052785,4.613512,2.214521,2.699086,1.965932,4.671854,2.886327,4.766762,3.729428,1.98722,9.678126]),
array([4.591795,4.879627,2.64143,4.693912,2.827498,4.074115,3.32711,3.400917,2.735957,3.198428,4.343812,2.553321,3.393799,2.317151,3.825602,2.966958,2.603105,1.95874,3.386157,3.991131,3.838364,4.028206,2.07818,2.452776,3.176425,2.088425,3.870645,3.269075]),
array([4.399182]),
array([4.919765,9.577133,5.810334,19.527625,14.517873,10.014154,16.840949,4.716384,7.153392,2.915274,3.008331,4.404059,2.868669,2.136553,4.658935,3.379538]),
array([12.095149,15.022739,12.801352,13.15755,12.922321,12.044625,22.778026,10.915435]),
array([5.630293,4.977587,4.806504]),
array([8.226518,7.373844,7.496277]),
array([7.709732,9.83588,14.460001,7.824699,9.665612,7.990739,9.532524,6.659259,10.177381,7.595462,22.084756,6.199449,12.861986,9.005286,8.019166,7.904342,13.302969,13.306131]),
array([9.844621,19.19127,6.718156,7.006981,9.969469,5.99223,8.169527,8.818444,9.435878,6.462169,6.179333,17.371675,21.509419,6.188261,18.266582,9.783464,13.578692,7.498797,11.788982,21.587718,12.199646,7.094476,5.995458,9.969374,4.949739,7.757027,7.994546,6.325563,7.097032]),
array([20.669907]),
array([34.291249,36.773946,36.893621,33.594288,32.876123,26.428885,25.423955,24.248012,21.783026,27.446646,25.405747,25.992149,25.798238,28.048084,22.962976,27.511754,23.046698,20.191266,17.206246,16.162355,10.691976,15.181833,8.624618,13.928071,5.686495,10.449415,12.273386,8.062479,13.842899,12.648357,14.910662,15.171908,9.813299,15.859375,11.434989,9.85389,14.239996,14.788161,15.821119,10.535773,15.780943,19.223048,17.551813,17.42784,14.536079,5.638837,15.539705,4.343058,3.339698,3.067692,3.70981,3.072222,2.09666,4.283504,4.107948,4.399568,2.641188,0.807155,0.839943,0.863915,1.351602,0.877297,1.323267,1.20211,3.994031,2.855946,6.644744,11.64181,2.714623,1.016659,0.714036,3.364898,3.250792,1.889684,1.131174,2.573863,0.216571,0.22365,0.338555,2.05269,1.03625,0.592591,7.108592,3.24413,16.74669,4.560514,11.747674,12.65601,0.31149,2.562852,4.266384,2.941586,26.41334,2.842638,3.395919,6.716108,3.239629,0.213104,16.885738,0.76232,5.941532,0.565419,1.938056,4.009189,0.088817,0.032786,0.013498,1.428423,0.034507,0.012186,0.107471,0.015023,0.099879,3.218642,0.197338,2.772649,0.09236,0.10947,0.019131,21.976688,21.618803,29.361973,28.758765,12.333144,0.894366]),
array([25.996502,6.11291,12.88799,11.77118,13.252076,13.574531,11.203379,6.4082,15.409467,5.372836,13.210964,10.923973,11.457944,6.96192,12.755228,11.734536,7.762607,13.462393,11.061006,10.893251,12.734451,12.504005,12.371451,12.67795,11.406153,3.586437,0.043362,0.093766,1.432682]),
array([5.50875,7.928513,6.839953,2.985474,4.764643,2.352045,3.055562,4.179802,3.513693,1.982364]),
array([8.740502,3.280176,8.161026,4.530174,2.982676,4.306882,4.603893,2.173945,2.697589,2.69346,0.681381,1.554986,1.007793,1.228536,1.252729,1.065128,0.970346,1.65871,0.282379,0.995113,1.582979,0.866223,1.506301,0.038672,3.418215,3.254936,3.267823,3.125387,2.293759,3.502354,2.903306,3.153451,4.94233,2.70588,3.22649,2.161756,0.001381,0.885099,1.580495,17.478051,4.682582,0.852484,0.004657,0.006162,0.002361,1.234314,0.001785,0.011156,0.001555,0.2329,0.115902,3.956656,1.443357,0.940215,0.009092,0.00516,0.002815,0.008596,1.107595,0.006051,2.380718,0.653799,0.009071,18.971287,3.744531,3.041784,3.577308,4.871378,4.338314,1.412931,2.000774,2.247451,1.1945,1.887569,2.547178,0.231556,0.771293,1.159482,2.63376,0.120799,0.765325,2.857852,4.811283,2.219557,0.958858,2.761323,1.601643,2.312322,1.696264,2.030922,2.560829,0.935907,1.185889,1.418672,2.279155,2.215597,1.215262,1.120623,1.720612,1.547347,2.209142,0.580518,2.602764,0.306368,0.154736,3.111897,2.544742,2.866077,2.953025,2.764089,3.060276,0.958371,1.799829,2.086369,1.339493,0.645649,0.408028,4.674541,4.849903,0.987231,2.013926,0.323303,1.575088,2.564484,1.368932,0.018805,1.99795,1.872263,3.083519,3.759516,3.376547,1.455276,1.6315,2.606837,4.806828,4.752668,4.807765,2.358702,2.069209,1.867495,0.492256,3.057063,0.698079,7.982464,4.861727,2.350937,1.432615,0.974778,2.029913,1.71402,2.54027,0.29502,1.448573,0.168461,0.486284,0.343518,0.517595,0.744077,1.64691,0.412507,0.357491,0.426564,1.985917,1.820946,2.183578,2.81266,3.066145,3.113917,2.120812,1.435,1.271662,1.197554,2.155204,0.741714,0.603548,0.384703,0.456899,0.33044,0.555584,0.64891,0.170979,0.362029,3.408442,3.141381,2.497177,1.393608,0.724052,2.296243,2.096661,0.350773,2.574109,0.286859,4.854191,4.257977,4.802036,3.307874,3.825141,3.749208,3.074631,4.261191,4.527671,1.961054,3.638262,1.778535,1.191825,0.017503,0.093,0.07153,2.448557,2.404408,0.06508,0.012669,0.004091,0.08351,2.513799,2.854881,2.658832,2.254436,1.690575,1.257918,0.052327,0.096256,0.08131,0.092386,0.028517,0.089669,0.303838,1.17151,15.014332,3.661654,0.063053,0.058332,0.673143,0.036625,3.90808,0.027196,0.01115,1.789028,0.302585,0.006216,0.005036,0.008479,0.004918,10.371726]),
array([0.715651,0.140154,0.244652,0.110796,0.050492,0.174989,0.529125]),
array([0.001952,0.002893,0.712972,2.058901,3.460177,2.157344,0.655274,0.286659,0]),
array([1.137892,0.416856,0]),
array([1.103455]),
array([4.73947,1.639364,1.42819,0.659967,1.42515,1.067753,1.370125,1.607608,0.621289,1.111651,0.596839,1.720796,1.187296,0.070546,0.367689,0.824679,0.137143,0.619814]),
array([0.002489,0.784745,0.221598,1.223236,0.736556,0.006032,1.762645,0.771211,1.988702,2.913889,0.671543,0.680119,0.216388,0.00679,0]),
array([0.967823]),
array([0.850179,0.644793,0.315763,1.198011,0.907028,1.634998,0.693912,1.026938,0.308568,0.256255,1.229014,0.251237,1.131767,0.688738,1.529002,0.061526,0.11201,0.08777,0.089123,0.028682,0.023696,0.11659,0.224243,0.068762,0.012939,0.057866,0.090684,0.05369,0.06894,2.444587,0.235769,1.360014,0.024206,0.091691,0.061399,0.020514,0.016905,1.275133,0.049957,0.045298,0.12151,0.07931,0.690948,0.073931,0.082181,0.233661,0.150772,0.092631,0.051585,0.038459,0.060167,0.062276,0.046122,0.058406,0.043903,0.065618,0.052957,0.069089,0.048026,0.063263,0.098133,0.080682,0.113861,0.03785,0.051436,0.0765,0.089408,0.040668,0.050236,1.609911,1.522065]),
array([1.713349,2.100639,0.602613,0.53312,1.76052,1.566254,4.698901,1.388626,0.444227,0.517458,1.193278,1.68234,3.108322,1.232303,1.243,0.935017,1.770741,0.736993,3.07898,4.196706,3.78214,4.298236,1.52784,1.309424,0.791615,0.500712,0.878188,1.76846,0.851686,22.550254,3.553158]),
array([0.002135,0.840542,0.009868,0.006406,0.006666,0.011296,0.009583,0.011463,0.001636,0.108161,0.006147,0.001512,0.004991,0.00235,0.006008,0.003786,0]),
array([7.732843,9.025397,10.05026,5.076078,3.224206,4.635252,4.870926,4.426295,1.855237,2.393308,3.466104,1.838338,6.222939,5.146069,7.980033,10.014594,2.612217]),
array([2.705605,3.690977,2.578111,3.713059,3.327507,4.22152,1.93313,4.536573,2.050144,3.759284,1.276865,1.166381,1.340895,0.547153,1.218338,1.411863,0.688692,0.943462,1.042147,1.570409,1.726657,1.172123,1.754842,0.573011,0.766477,1.177346,1.042417,0.534953,1.503766,0.443855,1.169036,1.235434,0.621557,1.065525,0.806719,0.743793,1.738965,0.346871,0.229881,1.11711,1.326674,1.676817,1.056054,1.232649,1.556633,0.011843,0.064993,0.071744,0.052052,0.053247,0.091716,0.059988,0.051754,0.125151,0.092658,0.016599,0.108461,0.04917,0.013504,0.115831,0.008988,0.084757,0.106467,0.032527,0.008349,0.461297,0.044051,0.016457,0.100986,0.05537,0.025425,0.090591,0.06102,0.096573,0.1252,0.125319,0.033622,0.096302,0.059465,0.075261,0.083155,0.073928,0.034208,0.058272,0.115386,0.093765,0.071735,0.083041,0.076386,1.30007,1.478003,2.134041,0.306454,1.616125,0.007147,0]),
array([5.217675,3.11907,4.276324,2.087717,4.61363,4.366048,4.266937,4.626494,2.042037,3.952699,3.502466,3.456831,3.790345,3.097236,2.072137,3.572201,2.446572,4.751425,3.969605,3.553941,2.42415,2.272425,3.829806,2.972038,3.529193,2.528177,2.120768,2.648253,2.675708,2.266522,1.815822,3.107159,4.878961,3.737848,2.863254,0.12181]),
array([1.290886,1.703716,1.033954,0.885483,0.119086,0.114513,0.097411,0.099565,1.793273,2.229132,1.877946,1.249736,0.126108,0.760067,2.929524,1.735544,0.764924,0.741755,0.252533,1.289642,0.716429,0.621908,0.404923,1.380022,0.940459,2.411548,0.5906,0.722495,0.616443,0.646851,0.090306,0.084651,0.073548,0.102738,0.119086,2.241551,0.631648,0.620128,0.50856,0.477689,0.554653,1.946895,0.671853,0.072768,0.255736,0.252584,0.54097,0.861423,0.106725,0.708163,0.146372,0.600823,0.34967,0.138131,0.663302,0.30686,2.49289,0.363064,0.428895,0.414916,2.3967,0.44508,0.007534,0.002602,1.183014,0.562582,3.212003,0.094306,0.119908,0.059965,0.01579,0.046198,0.043355,0.112079,0.120012,0.052479,0.099005,0.024288,0.046456,0.12263,0.795197,0.113089,0.063616,0.113246,0.035893,0.084238,0.056696,0.007382,0.045069,0.135219,0.229303,0.036705,0.101501,0.019186,0.006848,0.010579,0.0018,0.599751,0.094644,0]),
array([1.277313,4.896943,4.939484,0.001308,0.005766,3.152625,0.848729,1.708585,3.381525,2.469141,1.295852,0.008898,0.923574,0.184767,0.008212,1.536884,2.078827,1.156628,1.73513,1.024262,0.466265,0.37642,1.049772,2.337984,0.947826,1.783725,1.104228,1.302379,0.556982,0.516658,3.76893,0.276473,0.728349,2.24604,1.821293,2.388478,0.512694,2.170412,2.13457,1.986931,2.071044,1.723215,0.009564,0.109073,0.111073,1.608001,1.670785,0.111488,0.104012,0.638749,2.325194,2.373771,0]),
array([1.201039]),
array([1.939103,4.686571,4.7321,0.857548,1.383525,0.647386,0.097138,0]),
array([2.771858]),
array([15.733134,16.839016,13.735136]),
array([12.588582,10.556894,14.686645,14.188439,14.921524,14.889266,15.713291,15.376952,15.50695,14.897528,15.531448,14.878268,15.639875,15.202137,10.809595,13.696191,14.531412]),
array([5.87173,7.627482,7.634355]),
array([11.964456,12.193442,11.076618,10.619393,13.107179,11.024203,12.039447,11.980802,13.33638,7.782823,14.743553,12.200427]),
array([11.162426,13.117866,11.506947,13.14536,12.000343,11.912961,11.322781,11.27186,5.350352,15.246894,14.801727]),
array([4.882905,2.866617]),
array([8.607218,3.888453]),
array([0.006225,0.038562,0.018846]),
array([41.207151]),
array([2.254494]),
array([1.788755,0.98425]),
array([2.299254,3.001894]),
array([26.34736]),
array([27.543142,22.827781,28.637939,21.614234,21.48019,9.789803,8.577193,25.359517,25.173122,25.486401]),
array([25.652919,23.308938,22.542625,21.771831,22.141641]),
array([2.521643]),
array([0.090943,0.174094,0.147504,0.641762,0.191512,0.580269,0.597249,0.549161,0.61324,0.547478,0.574416,0.046805,0.159446]),
array([1.533986,0.255912,0.073121]),
array([25.042456,23.574523,23.520245,23.110739,24.088531,21.612868,16.832275,17.469091,20.263123,19.738949,20.227799,18.512017,18.850833,17.476161,19.843873,16.910205,17.08941,16.363107,18.222796,17.807091,15.989555,19.826785,16.814315,17.955108,17.296243,16.786805,17.853044,16.713647,14.657468,16.492791,16.070042,16.670908,16.993448,19.569649,15.991585,17.5326,18.112208,17.203232,16.080136,19.692467,18.8024,16.078716,15.260887,14.340147,14.478749,13.976393,21.446218]),
array([18.22807,17.065643]),
array([15.706672,19.791154]),
array([24.498828]),
array([22.640213,22.851048,22.725573,28.989168,30.726674,24.459402]),
array([21.222585,22.180918,24.723206,27.358746]),
array([23.224072,30.337622,30.464301,28.642584,27.792419,29.027719,30.26344,29.098789,28.753601]),
array([16.344515,17.141549]),
array([10.522016,14.457245,7.51847]),
array([11.060171,10.832848,17.550958,13.544894,12.94126,10.470918,13.174114,12.726713,11.974779,10.364738,18.097885,12.17449,11.9886,10.879729,6.923823,7.611445]),
array([13.674886,15.570225,14.819964]),
array([15.525258,19.980731]),
array([15.858172,13.822048,14.067411,15.609612,14.696149,14.819204,15.460311]),
array([12.844836,12.583176,10.700723]),
array([14.829976]),
array([26.927499]),
array([32.937944,32.409615,31.534326,33.224318,33.113552,33.15908,31.170917,33.009458,24.953532,28.39357,29.057834,30.522678,20.44024,28.344016]),
array([28.834134,32.581283,29.584761,41.074568,36.540233,36.189436,36.720389,54.751374,30.010289]),
array([35.190486,34.706788,34.606709,35.677278,34.297378]),
array([0.649829,0.190872,0.59882,0.745183,0.115561,1.450347]),
array([0.059175,0.768243,2.371647,0.598136]),
array([22.942084]),
array([19.113023,19.579926,17.207918,17.59604,19.386519,15.983455,20.319295,16.197777]),
array([24.210481,23.382947,20.739217,22.215001,22.600767,23.591277,22.1356,21.897855,22.144007,24.402834,21.332911,20.576482,21.615098,20.905258,24.717819,23.01879,24.714381,20.960041,23.21394,24.68784,21.936663,17.196975,19.807013,16.118662,16.063902,19.316611,18.752523,16.700675,17.686955,16.345365,27.181861,12.114878,19.349552]),
array([0.002834,0.003585,0.012716,1.238947,0.010413,0.010246,2.421033,0.066252]),
array([0.11885,0.313968,0.393957,0.096843,0.104168,0.032818,0.40895]),
array([0.803211]),
array([0.581252]),
array([31.721119,27.597211]),
array([23.593734]),
array([18.425018,17.814427,19.871825]),
array([31.458646,24.243776,21.183015,26.737003,25.484104,25.578286]),
array([21.582291]),
array([24.643089,21.774648,26.136441,30.323726,20.489776,21.874736,22.759461,23.117829]),
array([21.262791,21.54925,26.796768,26.115552,25.202324,30.543541,28.904636,29.171827,22.133356,25.294016]),
array([27.729809,21.374239]),
array([9.344066,5.862988,12.209812,5.086508,4.921915]),
array([8.258015]),
array([18.0669,7.541501,7.782539,20.780817,5.145039,9.982449,7.567373,11.801221,13.04802,10.848376,21.126274,5.952519,7.221903,12.310487,10.985869,10.36802,6.421963,13.142223,10.32465,12.135689,10.730997,13.467708,19.888882,6.712739,5.802538,11.845315,11.007561,7.126405,5.463655,8.356871,13.34251,14.996543,11.569831,10.613857,11.122273,5.219447,11.471022,5.275422,10.095282,16.83203,9.237701,8.323215,12.46416,7.122889,8.042068,8.033399,11.801311,18.685668,18.292581,20.293731,15.18308,12.059676,7.975751,9.526334,6.497621,11.118603,10.182973,10.943904,14.49466,15.323193,16.910549,8.860481,12.058404,11.690393,13.698363,7.806609,8.141861]),
array([12.671591,6.524648,9.784495,10.518146,12.215145,12.605768,13.282816,6.352997,7.361159,8.282788,11.577518,12.796281,12.638583,12.633264,12.824462,12.024829,13.341507,10.622676,13.566122,10.381302,10.407446,11.146742,10.566552,12.338225,11.949365,12.872463,10.377645,8.596307,8.239133,11.047978,7.760638,12.808778,13.290694,12.606655,12.237426,8.230943,11.109632,12.606796,12.74225,11.457743,12.77011,5.630445,11.384446,12.477099,13.263705,9.867241,12.397914,12.514589,13.04189,11.148788,10.671659,12.443324,13.323416,9.855087,6.371291,13.678815,15.944851,13.680098,13.892729,13.926471,14.387154,11.876917,20.845332,13.167682,6.114694,18.044272,11.913008,11.273206,9.071875,10.758573,10.827708,10.955291,12.927841,15.453933,6.0787,18.135987]),
array([8.268493,2.93605,5.791026]),
array([6.674764,7.102625,9.951862,5.230565,9.632421,9.759097,8.258689,6.394512,9.449843,14.822914,9.584217,9.105343,8.172293,5.524949,8.581487,7.938048,7.791404,2.2134,3.623926,5.443529,5.998522,7.37384,6.833591,10.270925,5.245492,7.357412,5.066507,8.271169]),
array([12.123651]),
array([15.222943,19.225622,18.409524,14.800518,15.57703,14.172455]),
array([19.69566]),
array([8.508814,12.937787]),
array([40.487102,36.938303,36.507939,36.337013,35.938831,34.956143,36.212868,37.188993,35.778628,35.82529,35.050302,34.930694,34.34554,34.604964,34.28768,34.905029,35.693458,33.898638,33.657806,33.877168,33.569528,33.81646,33.592221,33.584987,33.540593,33.327291,33.454012,25.648834,31.292307,31.689683,32.347749,32.926353,32.018853,28.264285]),
array([33.768799,33.495367]),
array([39.601559,36.963155,35.13647,34.924152,36.949729,34.071871,34.942762,35.802894,35.223092,33.906005,37.020164,35.001268,36.873934,35.107089,35.388901,36.607559,36.722495,36.736579,37.173053,36.473711,37.157046,35.126448,34.231085,33.918971,34.040202,35.563424,35.435857,36.798188,35.000072,34.173318,34.83843,34.915538,36.563297,34.790929,36.381688,36.182756,35.219032,34.874638,33.326031,33.658944,33.518887,33.551272,33.620277,33.346612,33.490893,33.421204,33.635464,33.33987,33.822734,33.500054,33.649947,33.554076,33.357275,33.585112,33.331607,33.561345,33.434939,33.543494,33.739514,33.70999,33.883251,33.546682,33.332043,33.376454,33.434438,33.745255,33.881483,33.690909,33.380841,33.525583,33.543764,33.742723,33.830997,33.807662,33.74743,33.6443,33.696805,33.37578,33.552371,33.715875,33.400696,33.6422,33.671643,33.312323,33.496521,33.821219,33.710511,33.419922,33.520891,33.842234,33.71782,33.770596,33.646843,33.618441,33.646011,33.802424,33.643499,33.66522,33.850705,33.591757,33.683367,33.439007,33.478389,33.338185,33.85926,33.394604,33.512299,33.873326,33.61984,33.594576,33.457038,33.673637,33.448381,33.763704,33.407014,33.747642,33.41226,33.838148,33.759911,33.769369,33.430084,33.451097,33.648005,31.765044,31.659837,31.322835,32.690623,31.40761,33.07508,31.002416,35.583058,36.722216,33.662281]),
array([28.149063,21.011949]),
array([24.447613,23.35285,13.600701,10.820386,13.860939,13.398809,13.330864,10.145981,14.257669,12.802457,22.834458,23.951717,13.946674]),
array([21.035466]),
array([29.759466,30.212957,29.56769,28.524708,28.420419]),
array([21.113875,24.772964,24.303673,20.930604,21.739598,20.96832]),
array([15.853291,16.299206,19.520922,19.059266,17.237404,24.138555,17.524872,16.21585,16.648117,18.995765,17.947905,16.127674,19.614226,16.645003,14.66585,15.530301,15.583921,14.537827,13.669727,15.608555,15.53406,13.801761,15.134483,14.208609]),
array([11.368593,11.203374,12.412701,12.477273,13.142173,13.295863,13.330941,10.344431,12.214675,7.953258,11.756329,11.030495,11.680438,10.772032,10.930532,12.149303,13.505153,12.421774]),
array([29.306807]),
array([13.185833]),
array([14.150154,13.784099,17.785464,12.863763,14.485493,15.210698,12.270456,13.994513,14.610077,14.587505,15.891206,14.772205,15.936033,15.845511,14.777093,15.398555,15.466392,11.813126,15.778019,14.349042,15.108584,12.883766,14.806948,10.822924,13.453912,12.243685,12.903909,12.336548,10.310423,15.634398,15.885991,13.753926,15.540836,13.694968,15.703967,10.742487,11.662444,10.508638,13.364407,11.556558,10.377964,12.104984,14.311259,19.028491,10.367903,5.861136,13.498909,20.697953,17.631482,10.363947,12.680406]),
array([21.469623,16.800092,22.255489,18.986119,20.097292,26.139932]),
array([1.156002,0.222816,2.513296,4.608448,0.363446,0.708827,3.219085]),
array([0.011111,1.972388,0.941118,0.609254,0.340285,0.956779,2.186111,0.858127,1.531871,0.02657]),
array([24.106362]),
array([23.910643,26.276025,25.165483,21.96439,22.877708]),
array([20.848529,29.547113]),
array([33.771147,31.009887,31.825801,32.900835,31.121003,32.667057,31.590976,31.373485,30.883663,30.82815,32.512125,31.360556,33.161813,31.814952,26.736058,29.684439,30.490406,29.565864,29.177893,25.801591,24.329349]),
array([7.526019]),
array([12.616246,15.260258,8.497361]),
array([6.047186,8.3489,8.899678,7.963717,13.465633,18.946556]),
array([15.478248]),
array([17.031065,17.624856,20.160529,17.373211,16.011692,17.052209,16.647638,19.946066,19.721324,16.512246,18.167242,17.715263,19.748957,19.500568,17.091329,18.260395,18.520039,17.615684,18.095987,19.464236,16.391653,17.732554,20.095725,17.848001,18.762496]),
array([19.205301,14.914389,17.441239,17.042113,19.227131,19.063709,16.65467,17.74862,15.330598,12.900626,10.143051,12.558337,14.428076,16.139837,15.958991,21.246926,14.378854,14.6926,14.584395,7.18565,15.793681,15.918701,14.930633,15.306166,15.333297,15.523012,6.795148,15.531252,13.974222,14.500351,14.754218,14.62669,13.676809,15.864049]),
array([41.369787]),
array([5.06753,0.753901,3.003119,2.971486,2.356846,3.032869,3.06168,0.374418,5.318893,3.904883,3.650602,3.851427,1.558765,3.906609,3.809284,3.834008,2.285057,4.565586,6.571092,4.897972,3.653827,3.636001,5.041127,2.850841,2.065565,2.467331,1.963461,2.289179,2.760621,2.033671,3.865733,1.626017,1.928797,4.763752,2.769807,4.237861,2.358212,2.100245]),
array([3.566129,2.727846]),
array([0.830369,0.03091,0.066776]),
array([24.091845,17.477708]),
array([15.560818,19.470897,19.189292,17.376875,16.787527,16.343802,16.09678,19.459857,16.37118,14.472117,14.058443,15.105954,14.920611,14.782304]),
array([18.804049,17.582592,18.38898,20.12927]),
array([33.718523,32.867155]),
array([20.251716,16.769726,18.845836]),
array([32.308767,31.037604,25.539144]),
array([25.665427]),
array([28.536222,24.098005,24.983323,25.268139,28.568975,28.428931]),
array([33.869863,33.637282]),
array([0.237012,0.480621,3.018116,0.152237,1.517199]),
array([0.008656,0.006746,0.233441,0.236513,0.650673,2.240103,0.027453]),
array([30.932664,30.806364]),
array([30.915182,33.118605,31.643481,31.668477]),
array([19.849538,16.079606,11.027708,19.63248,18.28097,16.025806,15.972933,18.927044,17.19165,19.65534,15.578376,14.809981,17.240067,16.03718,13.616037,16.402624,13.752616,13.849839]),
array([17.91204,19.694066,17.009254,15.515414,20.084515]),
array([23.786774,25.719053,27.104504,23.161095,24.790464,23.719536,27.572791,22.281571,22.776747,22.101569,20.667745,25.384819]),
array([21.003512,23.276532]),
array([21.398504,22.78932,24.158429,24.501026,22.053735,23.025453,25.264366,21.765279]),
array([11.6883,13.086452,13.524152,6.90568,13.37145,12.487693,11.406316,12.755955,10.743773,11.08608,13.397654,13.001604,10.595299,10.522678,10.834967,12.642971,12.497281,10.723603,13.210888,11.865824,15.65154,13.358557,13.471039,10.548667,12.917441,10.644289]),
array([14.91403,14.34522,14.509254,14.812986,15.65474,14.003494,15.458003,14.241088,14.109731,13.860762,14.373311,15.416342,14.654482,13.661189,15.426344,5.234418,14.134135,15.75051,19.907442,15.901018,15.901081,14.938054,14.22144,14.406143,14.393123,15.764164,14.798633,14.297723,15.780137,14.602057,14.803457,15.105352,14.383953,14.204743,15.319204,13.579486,14.892353,15.519685,15.794755,14.348242,14.201459,14.643884,14.109888,13.959819]),
array([23.140344,28.705545,30.529181,29.846794,26.345059,27.685194,27.519816,28.985767]),
array([24.645959,21.420258,19.472707,20.273255,22.723108,17.458605,19.336621,20.038932,24.252603]),
array([20.566531]),
array([23.620672,21.168002,24.084229,23.10369,24.467625,22.066463,23.233242,22.636461]),
array([33.111386,29.407106,22.779823]),
array([23.790066,20.92891,17.388538,18.856726,19.47816,20.35919,19.315853,18.238305,19.406134]),
array([18.342375]),
array([19.624994,18.263112,15.979515,19.53837,16.881712]),
array([23.816191,25.89081,23.059387,21.271022,21.277117,21.486056,23.052892,22.038875,24.40747,20.89647,22.370213,18.153066]),
array([21.104177]),
array([21.956363,27.196037,27.418242,29.026442]),
array([19.006111]),
array([33.473308]),
array([14.257641,15.032069,15.467512,15.762368,13.94471]),
array([0.285215,1.572691,2.347894,0.059803,1.10912,0.038063,0.072592]),
array([0.520831]),
array([2.112718]),
array([0.491879,0.011796,0.086047,0.09415,2.319701,0.305473,0.090038,0.112231]),
array([15.991846,19.506577,16.821322,19.158295,19.135414,19.120136,20.23824,18.192137,18.414877,20.426894,16.014762,18.999647,16.336131,19.136809,17.756417,17.162249,16.075548,19.479738,16.410313,17.840823,15.316389,16.089626,17.362772,14.06206,14.99293,13.763248,19.481795]),
array([15.178799,19.204579,19.531106,15.285802]),
array([0.009236,1.080437,0.527946,0.082072,0]),
array([21.39348,24.994236,30.125572]),
array([1.799115]),
array([0.008408]),
array([29.524277,25.630931,28.461255,27.2747,29.618331]),
array([14.274019,14.038309,7.570141]),
array([0.089891,2.143933,0.08172]),
array([3.027831,3.740343]),
array([15.241804,14.194261,17.159499,14.573079,12.632338]),
array([17.695206,17.414553,19.287034,17.642817,15.218477,19.882992,17.066594,19.609807,17.274679,18.061224,19.86983,14.659397,22.767801,14.746578,6.264692,15.454338,14.757084,16.148336,17.272801,14.806928]),
array([16.189871,19.69654,18.555405,15.546734,19.118063,17.880461,19.108198,16.374171,16.39903,18.525652,18.529063,13.98584,19.347481,18.942964,18.036695,18.181643,13.774252,14.19785,15.661035,14.648878,13.634509,15.432291,15.169504,13.876814,15.87496,15.716967,14.084839,14.026444,15.8983,15.642891,14.725278,14.429968,15.668628,16.445558,15.102495]),
array([2.339816,0.312921,0.896925,1.106003,0.031644,0.023229,0.070854,0.013865,0.225697,13.331924]),
array([3.461821,0.455673,0.860574,1.015415,0.769126,1.345296,1.326274,0.214055,1.186683,0.065118,0.031627,0.015248,0.118076,0.083081,0.817522,0.032738,1.240669,0.073548,0.034139,0.118154,0.125758,1.261106,0.117205,0.095944,1.539797,0.087887,0.011089,0.028107,0.014679,0.075403,0.114355,0.089619,0.034354,0.083276]),
array([4.892769]),
array([1.835734,4.548983,3.868119,3.111525,4.176616]),
array([1.118871,1.075964]),
array([3.629315]),
array([10.133884]),
array([7.242931,6.798647,5.858951,8.69338,3.870846,1.306123,1.748379,1.41215,1.185794,1.073703,0.374193,0.52145,0.740915,1.616849,0.015223,1.626345,4.363332,5.000168,1.349611,1.637654,0.213608,3.513815,1.373197,3.311158,2.754284,2.886981,2.620708,1.829007,1.982977,1.306465,0.390882,2.246964,4.01193,1.179904,2.755807,3.189888,0.690054,1.885534,1.260274,1.264005,1.907122,2.161756,5.001549,1.384254,2.365491,1.07528,3.134155,1.426345,3.03283,3.11221,3.097374,2.640256,2.708046,4.6441,2.16709,2.452166,2.213872,1.224521,0.445255,0.359792,1.259602,1.780125,0.809353,0.195665,1.536974,3.339464,0.114048,1.023121,1.415066,1.334109,2.584496,1.857799,3.895277,5.889478,3.749865,2.528417,1.21467,0.556563,3.928371,0.0929,0.019636,0.019909,0.19995,0.454967,1.090189,0.242754,0.57948,1.496927,4.526744,3.102813,2.082986,1.23038,0.128989,0.778562,0.727824,2.457159,0.220932,3.637184,3.374379,1.541733,2.314781,0.072077,0.028589,0.083288,3.6448,1.455556,4.125127,0.045095,0.034867,0.014675,0.278321,4.813521,2.385508,0.965815,0.111239,0.004676]),
array([0.058409]),
array([0.005562,0.981649,0.008274,2.357889,0.001187,0.008861,0.008794,1.915371,0.01061,0.01072,0.008257,2.08012,1.188492,0.641421,2.296004,1.207672,0.053447,0.096571,0.813356,2.09866]),
array([10.487575]),
array([3.856429]),
array([7.973647,10.187622,9.065064,8.790488,6.923336,8.722404,8.22087,7.285175,7.236516,8.878252,9.852694,0.993478,7.19129,5.41374,6.420306,6.558471,8.875578,6.733058,10.101997,6.867491,14.630492]),
array([4.038043,0.637649,1.310465,0.940078,0.864913,0.377446,0.370301,0.55662,0.332674,0.069793,0.053207,0.062809,0.083667,0.03928,0.076402]),
array([1.041782,0.957021,0.788854,1.182353,0.094917,0.015826,0.056368,0.037131,2.150633,0.552885,0.214461,0.158323,0.533561,0.650422,0.021174,0.281407,0.405548,0.718857,0.461411,3.037146,1.228146,0.091437,0.420579,0.396879,0.097973,0.521152,0.667629,0.141723,0.115449,0.171003,0.137186,0.125538,1.281018,0.863166,2.184056,0.057161,1.076672,0.709872,0.252203,0.750798,1.496079,0.358559,0.112888,0.118121,0.319862,0.100432,0.083604,0.107989,0.099631,0.023849,0.013868,0.062138,0.021057,0.04014,0.120374,0.092677,0.117074,0.088312,0.041517,1.659822,0.028755,0.007741,0.001495,0.010184,0.057512,1.148989,0.065638]),
array([0.027392]),
array([0.02065]),
array([0.392936,1.029387,0.502206]),
array([0.944022,2.128321,0.12255,2.02841,0.507759,1.670946,0.237894,1.102711,0.398462]),
array([1.551249])
]

d=[data_1]
names=[ 'canid_occ_1']
def get_data(i): return d[i]
def get_out_name(i): return  names[i]
taxa_names=['Aelurodon','Aelurodon_asthenostylus','Aelurodon_ferox','Aelurodon_mcgrewi','Aelurodon_montanensis','Aelurodon_stirtoni','Aelurodon_taxoides','Aelurodon_wheelerianus','Alopex','Alopex_lagopus','Archaeocyon_falkenbachi','Archaeocyon_leptodus','Archaeocyon_pavidus','Borophaginae','Borophagus','Borophagus_diversidens','Borophagus_dudleyi','Borophagus_hilli','Borophagus_littoralis','Borophagus_orc','Borophagus_parvus','Borophagus_pugnator','Borophagus_secundus','Caedocyon_tedfordi','Canidae','Caninae','Canini','Canis','Canis_(Pseudalopex)','Canis_adustus','Canis_anthus','Canis_apolloniensis','Canis_armbrusteri','Canis_aureus','Canis_cedazoensis','Canis_dirus','Canis_edwardii','Canis_familiaris','Canis_ferox','Canis_latrans','Canis_lepophagus','Canis_lupus','Canis_mesomelas','Canis_proplatensis','Canis_rufus','Canis_thooides','Carpocyon','Carpocyon_compressus','Carpocyon_limosus','Carpocyon_robustus','Carpocyon_webbi','Cerdocyon_avius','Cerdocyon_texanus','Cerdocyon_thous','Chailicyon_crassidens','Chrysocyon','Chrysocyon_brachyurus','Chrysocyon_nearcticus','Cormocyon','Cormocyon_copei','Cormocyon_haydeni','Cubacyon_transversidens','Cuon','Cuon_alpinus','Cynarctoides_acridens','Cynarctoides_emryi','Cynarctoides_gawnae','Cynarctoides_harlowi','Cynarctoides_lemur','Cynarctoides_luskensis','Cynarctoides_roii','Cynarctoides_whistleri','Cynarctus','Cynarctus_crucidens','Cynarctus_galushai','Cynarctus_marylandica','Cynarctus_saxatilis','Cynarctus_voorhiesi','Cynarctus_wangi','Cynodesmus_martini','Cynodesmus_thooides','Cynodictis','Cynodictis_lacustris','Cynotherium','Cynotherium_sardous','Desmocyon','Desmocyon_matthewi','Desmocyon_thomsoni','Dusicyon','Dusicyon_avus','Dusicyon_culpaeus','Dusicyon_sechurae','Ectopocynus_antiquus','Ectopocynus_intermedius','Ectopocynus_simplicidens','Enhydrocyon','Enhydrocyon_basilatus','Enhydrocyon_crassidens','Enhydrocyon_pahinsintewakpa','Enhydrocyon_stenocephalus','Epicyon','Epicyon_aelurodontoides','Epicyon_haydeni','Epicyon_saevus','Eucyon','Eucyon_davisi','Eucyon_skinneri','Euoplocyon_brachygnathus','Euoplocyon_spissidens','Gobicyon','Hesperocyon','Hesperocyon_coloradensis','Hesperocyon_gregarius','Hesperocyoninae','Leptocyon','Leptocyon_delicatus','Leptocyon_douglassi','Leptocyon_gregorii','Leptocyon_leidyi','Leptocyon_matthewi','Leptocyon_mollis','Leptocyon_tejonensis','Leptocyon_vafer','Leptocyon_vulpinus','Lycaon','Lycaon_pictus','Mesocyon','Mesocyon_brachyops','Mesocyon_coryphaeus','Mesocyon_temnodon','Metalopex_bakeri','Metalopex_macconnelli','Metalopex_merriami','Metatomarctus','Metatomarctus_canavus','Microtomarctus_conferta','Neovulpavus_washakius','Nyctereutes','Nyctereutes_abdeslami','Nyctereutes_procyonoides','Osbornodon_brachypus','Osbornodon_fricki','Osbornodon_iamonensis','Osbornodon_renjiei','Osbornodon_scitulus','Osbornodon_sesnoni','Osbornodon_wangi','Otarocyon_cooki','Otarocyon_macdonaldi','Otocyon','Otocyon_megalotis','Oxetocyon','Oxetocyon_cuspidatus','Paracynarctus_kelloggi','Paracynarctus_sinclairi','Paraenhydrocyon_josephi','Paraenhydrocyon_robustus','Paraenhydrocyon_wallovianus','Paratomarctus_euthos','Paratomarctus_temerarius','Philotrox_condoni','Phlaocyon','Phlaocyon_achoros','Phlaocyon_annectens','Phlaocyon_latidens','Phlaocyon_leucosteus','Phlaocyon_mariae','Phlaocyon_marslandensis','Phlaocyon_minor','Phlaocyon_multicuspus','Phlaocyon_taylori','Phlaocyon_yatkolai','Protemnocyon_inflatus','Protepicyon_raki','Protocyon','Protocyon_orcesi','Protocyon_tarijensis','Protocyon_troglodytes','Protomarctus_optatus','Psalidocyon_marianae','Pseudalopex_gymnocercus','Rhizocyon_oregonensis','Speothos','Speothos_venaticus','Sunkahetanka_geringensis','Tephrocyon_rurestris','Theriodictis','Theriodictis_floridanus','Tomarctus','Tomarctus_brevirostris','Tomarctus_hippophaga','Urocyon','Urocyon_cinereoargenteus','Urocyon_citrinus','Urocyon_galushai','Urocyon_minicephalus','Urocyon_progressus','Urocyon_webbi','Vulpes','Vulpes_cascadensis','Vulpes_chama','Vulpes_kernensis','Vulpes_mathisoni','Vulpes_stenognathus','Vulpes_velox','Vulpes_vulpes','Vulpes_vulpes_macroura','Vulpini','Xenocyon','Xenocyon_lycaonoides','Xenocyon_texanus']
def get_taxa_names(): return taxa_names
