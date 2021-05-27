import string
from pathlib import Path

class AUDIO_CONFIG:
    sampling_rate = 32000
    duration = 1
    hop_length = 251 # making it 128 in size
    fmin = 500
    fmax = 15000
    n_mels = 128
    n_fft = n_mels * 20
    samples = sampling_rate * duration
    padmode = 'reflect'
    
def fill_range(letter_start, letter_end, path_fill, dict_val={}):
    alphabet = list(string.ascii_lowercase)
    for a in alphabet[alphabet.index(letter_start):alphabet.index(letter_end)+1]:
        dict_val[a] = path_fill
    return dict_val

def get_dict_value(input_dir):
    dict_val = {}
    dict_val = fill_range('a','z',input_dir,dict_val)
    #dict_val = fill_range('c','f',input_dir/"birdsong-resampled-train-audio-01",dict_val)
    #dict_val = fill_range('g','m',input_dir/"birdsong-resampled-train-audio-02",dict_val)
    #dict_val = fill_range('n','r',input_dir/"birdsong-resampled-train-audio-03",dict_val)
    #dict_val = fill_range('s','y',input_dir/"birdsong-resampled-train-audio-04",dict_val)
    return dict_val

BIRD_CODE = {
    'acafly': 0, 'acowoo': 1, 'aldfly': 2, 'ameavo': 3, 'amecro': 4, 'amegfi': 5,
    'amekes': 6, 'amepip': 7, 'amered': 8, 'amerob': 9, 'amewig': 10,
    'amtspa': 11, 'andsol1': 12, 'annhum': 13, 'astfly': 14, 'azaspi1': 15,
    'babwar': 16, 'baleag': 17, 'balori': 18, 'banana': 19, 'banswa': 20,
    'banwre1': 21, 'barant1': 22, 'barswa': 23, 'batpig1': 24, 'bawswa1': 25,
    'bawwar': 26, 'baywre1': 27, 'bbwduc': 28, 'bcnher': 29, 'belkin1': 30,
    'belvir': 31, 'bewwre': 32, 'bkbmag1': 33, 'bkbplo': 34, 'bkbwar': 35,
    'bkcchi': 36, 'bkhgro': 37, 'bkmtou1': 38, 'bknsti': 39, 'blbgra1': 40,
    'blbthr1': 41, 'blcjay1': 42, 'blctan1': 43, 'blhpar1': 44, 'blkpho': 45,
    'blsspa1': 46, 'blugrb1': 47, 'blujay': 48, 'bncfly': 49, 'bnhcow': 50,
    'bobfly1': 51, 'bongul': 52, 'botgra': 53, 'brbmot1': 54, 'brbsol1': 55,
    'brcvir1': 56, 'brebla': 57, 'brncre': 58, 'brnjay': 59, 'brnthr': 60,
    'brratt1': 61, 'brwhaw': 62, 'brwpar1': 63, 'btbwar': 64, 'btnwar': 65,
    'btywar': 66, 'bucmot2': 67, 'buggna': 68, 'bugtan': 69, 'buhvir': 70,
    'bulori': 71, 'burwar1': 72, 'bushti': 73, 'butsal1': 74, 'buwtea': 75,
    'cacgoo1': 76, 'cacwre': 77, 'calqua': 78, 'caltow': 79, 'cangoo': 80,
    'canwar': 81, 'carchi': 82, 'carwre': 83, 'casfin': 84, 'caskin': 85,
    'caster1': 86, 'casvir': 87, 'categr': 88, 'ccbfin': 89, 'cedwax': 90,
    'chbant1': 91, 'chbchi': 92, 'chbwre1': 93, 'chcant2': 94, 'chispa': 95,
    'chswar': 96, 'cinfly2': 97, 'clanut': 98, 'clcrob': 99, 'cliswa': 100,
    'cobtan1': 101, 'cocwoo1': 102, 'cogdov': 103, 'colcha1': 104, 'coltro1': 105,
    'comgol': 106, 'comgra': 107, 'comloo': 108, 'commer': 109, 'compau': 110,
    'compot1': 111, 'comrav': 112, 'comyel': 113, 'coohaw': 114, 'cotfly1': 115,
    'cowscj1': 116, 'cregua1': 117, 'creoro1': 118, 'crfpar': 119, 'cubthr': 120,
    'daejun': 121, 'dowwoo': 122, 'ducfly': 123, 'dusfly': 124, 'easblu': 125,
    'easkin': 126, 'easmea': 127, 'easpho': 128, 'eastow': 129, 'eawpew': 130,
    'eletro': 131, 'eucdov': 132, 'eursta': 133, 'fepowl': 134, 'fiespa': 135,
    'flrtan1': 136, 'foxspa': 137, 'gadwal': 138, 'gamqua': 139, 'gartro1': 140,
    'gbbgul': 141, 'gbwwre1': 142, 'gcrwar': 143, 'gilwoo': 144, 'gnttow': 145,
    'gnwtea': 146, 'gocfly1': 147, 'gockin': 148, 'gocspa': 149, 'goftyr1': 150,
    'gohque1': 151, 'goowoo1': 152, 'grasal1': 153, 'grbani': 154, 'grbher3': 155,
    'grcfly': 156, 'greegr': 157, 'grekis': 158, 'grepew': 159, 'grethr1': 160,
    'gretin1': 161, 'greyel': 162, 'grhcha1': 163, 'grhowl': 164, 'grnher': 165,
    'grnjay': 166, 'grtgra': 167, 'grycat': 168, 'gryhaw2': 169, 'gwfgoo': 170,
    'haiwoo': 171, 'heptan': 172, 'hergul': 173, 'herthr': 174, 'herwar': 175,
    'higmot1': 176, 'hofwoo1': 177, 'houfin': 178, 'houspa': 179, 'houwre': 180,
    'hutvir': 181, 'incdov': 182, 'indbun': 183, 'kebtou1': 184, 'killde': 185,
    'labwoo': 186, 'larspa': 187, 'laufal1': 188, 'laugul': 189, 'lazbun': 190,
    'leafly': 191, 'leasan': 192, 'lesgol': 193, 'lesgre1': 194, 'lesvio1': 195,
    'linspa': 196, 'linwoo1': 197, 'littin1': 198, 'lobdow': 199, 'lobgna5': 200,
    'logshr': 201, 'lotduc': 202, 'lotman1': 203, 'lucwar': 204, 'macwar': 205,
    'magwar': 206, 'mallar3': 207, 'marwre': 208, 'mastro1': 209, 'meapar': 210,
    'melbla1': 211, 'monoro1': 212, 'mouchi': 213, 'moudov': 214, 'mouela1': 215,
    'mouqua': 216, 'mouwar': 217, 'mutswa': 218, 'naswar': 219, 'norcar': 220,
    'norfli': 221, 'normoc': 222, 'norpar': 223, 'norsho': 224, 'norwat': 225,
    'nrwswa': 226, 'nutwoo': 227, 'oaktit': 228, 'obnthr1': 229, 'ocbfly1': 230,
    'oliwoo1': 231, 'olsfly': 232, 'orbeup1': 233, 'orbspa1': 234, 'orcpar': 235,
    'orcwar': 236, 'orfpar': 237, 'osprey': 238, 'ovenbi1': 239, 'pabspi1': 240,
    'paltan1': 241, 'palwar': 242, 'pasfly': 243, 'pavpig2': 244, 'phivir': 245,
    'pibgre': 246, 'pilwoo': 247, 'pinsis': 248, 'pirfly1': 249, 'plawre1': 250,
    'plaxen1': 251, 'plsvir': 252, 'plupig2': 253, 'prowar': 254, 'purfin': 255,
    'purgal2': 256, 'putfru1': 257, 'pygnut': 258, 'rawwre1': 259, 'rcatan1': 260,
    'rebnut': 261, 'rebsap': 262, 'rebwoo': 263, 'redcro': 264, 'reevir1': 265,
    'rehbar1': 266, 'relpar': 267, 'reshaw': 268, 'rethaw': 269, 'rewbla': 270,
    'ribgul': 271, 'rinkin1': 272, 'roahaw': 273, 'robgro': 274, 'rocpig': 275,
    'rotbec': 276, 'royter1': 277, 'rthhum': 278, 'rtlhum': 279, 'ruboro1': 280,
    'rubpep1': 281, 'rubrob': 282, 'rubwre1': 283, 'ruckin': 284, 'rucspa1': 285,
    'rucwar': 286, 'rucwar1': 287, 'rudpig': 288, 'rudtur': 289, 'rufhum': 290,
    'rugdov': 291, 'rumfly1': 292, 'runwre1': 293, 'rutjac1': 294, 'saffin': 295,
    'sancra': 296, 'sander': 297, 'savspa': 298, 'saypho': 299, 'scamac1': 300,
    'scatan': 301, 'scbwre1': 302, 'scptyr1': 303, 'scrtan1': 304, 'semplo': 305,
    'shicow': 306, 'sibtan2': 307, 'sinwre1': 308, 'sltred': 309, 'smbani': 310,
    'snogoo': 311, 'sobtyr1': 312, 'socfly1': 313, 'solsan': 314, 'sonspa': 315,
    'soulap1': 316, 'sposan': 317, 'spotow': 318, 'spvear1': 319, 'squcuc1': 320,
    'stbori': 321, 'stejay': 322, 'sthant1': 323, 'sthwoo1': 324, 'strcuc1': 325,
    'strfly1': 326, 'strsal1': 327, 'stvhum2': 328, 'subfly': 329, 'sumtan': 330,
    'swaspa': 331, 'swathr': 332, 'tenwar': 333, 'thbeup1': 334, 'thbkin': 335,
    'thswar1': 336, 'towsol': 337, 'treswa': 338, 'trogna1': 339, 'trokin': 340,
    'tromoc': 341, 'tropar': 342, 'tropew1': 343, 'tuftit': 344, 'tunswa': 345,
    'veery': 346, 'verdin': 347, 'vigswa': 348, 'warvir': 349, 'wbwwre1': 350,
    'webwoo1': 351, 'wegspa1': 352, 'wesant1': 353, 'wesblu': 354, 'weskin': 355,
    'wesmea': 356, 'westan': 357, 'wewpew': 358, 'whbman1': 359, 'whbnut': 360,
    'whcpar': 361, 'whcsee1': 362, 'whcspa': 363, 'whevir': 364, 'whfpar1': 365,
    'whimbr': 366, 'whiwre1': 367, 'whtdov': 368, 'whtspa': 369, 'whwbec1': 370,
    'whwdov': 371, 'wilfly': 372, 'willet1': 373, 'wilsni1': 374, 'wiltur': 375,
    'wlswar': 376, 'wooduc': 377, 'woothr': 378, 'wrenti': 379, 'y00475': 380,
    'yebcha': 381, 'yebela1': 382, 'yebfly': 383, 'yebori1': 384, 'yebsap': 385,
    'yebsee1': 386, 'yefgra1': 387, 'yegvir': 388, 'yehbla': 389, 'yehcar1': 390,
    'yelgro': 391, 'yelwar': 392, 'yeofly1': 393, 'yerwar': 394, 'yeteup1': 395,
    'yetvir': 396
}

EBIRD_LABEL = {
    'acafly': 'Acadian Flycatcher',
    'acowoo': 'Acorn Woodpecker',
    'aldfly': 'Alder Flycatcher',
    'ameavo': 'American Avocet',
    'amecro': 'American Crow',
    'amegfi': 'American Goldfinch',
    'amekes': 'American Kestrel',
    'amepip': 'American Pipit',
    'amered': 'American Redstart',
    'amerob': 'American Robin',
    'amewig': 'American Wigeon',
    'amtspa': 'American Tree Sparrow',
    'andsol1': 'Andean Solitaire',
    'annhum': "Anna's Hummingbird", 'astfly': 'Ash-throated Flycatcher',
    'azaspi1': "Azara's Spinetail", 'babwar': 'Bay-breasted Warbler',
    'baleag': 'Bald Eagle',
    'balori': 'Baltimore Oriole',
    'banana': 'Bananaquit',
    'banswa': 'Bank Swallow',
    'banwre1': 'Banded Wren',
    'barant1': 'Barred Antshrike',
    'barswa': 'Barn Swallow',
    'batpig1': 'Band-tailed Pigeon',
    'bawswa1': 'Blue-and-white Swallow',
    'bawwar': 'Black-and-white Warbler',
    'baywre1': 'Bay Wren',
    'bbwduc': 'Black-bellied Whistling-Duck',
    'bcnher': 'Black-crowned Night-Heron',
    'belkin1': 'Belted Kingfisher',
    'belvir': "Bell's Vireo", 'bewwre': "Bewick's Wren", 'bkbmag1': 'Black-billed Magpie',
    'bkbplo': 'Black-bellied Plover',
    'bkbwar': 'Blackburnian Warbler',
    'bkcchi': 'Black-capped Chickadee',
    'bkhgro': 'Black-headed Grosbeak',
    'bkmtou1': 'Yellow-throated Toucan',
    'bknsti': 'Black-necked Stilt',
    'blbgra1': 'Blue-black Grassquit',
    'blbthr1': 'Black-billed Thrush',
    'blcjay1': 'Black-chested Jay',
    'blctan1': 'Black-capped Tanager',
    'blhpar1': 'Blue-headed Parrot',
    'blkpho': 'Black Phoebe',
    'blsspa1': 'Black-striped Sparrow',
    'blugrb1': 'Blue Grosbeak',
    'blujay': 'Blue Jay',
    'bncfly': 'Brown-crested Flycatcher',
    'bnhcow': 'Brown-headed Cowbird',
    'bobfly1': 'Boat-billed Flycatcher',
    'bongul': "Bonaparte's Gull", 'botgra': 'Boat-tailed Grackle',
    'brbmot1': 'Broad-billed Motmot',
    'brbsol1': 'Brown-backed Solitaire',
    'brcvir1': 'Brown-capped Vireo',
    'brebla': "Brewer's Blackbird", 'brncre': 'Brown Creeper',
    'brnjay': 'Brown Jay',
    'brnthr': 'Brown Thrasher',
    'brratt1': 'Bright-rumped Attila',
    'brwhaw': 'Broad-winged Hawk',
    'brwpar1': 'Bronze-winged Parrot',
    'btbwar': 'Black-throated Blue Warbler',
    'btnwar': 'Black-throated Green Warbler',
    'btywar': 'Black-throated Gray Warbler',
    'bucmot2': "Lesson's Motmot", 'buggna': 'Blue-gray Gnatcatcher',
    'bugtan': 'Blue-gray Tanager',
    'buhvir': 'Blue-headed Vireo',
    'bulori': "Bullock's Oriole", 'burwar1': 'Buff-rumped Warbler',
    'bushti': 'Bushtit',
    'butsal1': 'Buff-throated Saltator',
    'buwtea': 'Blue-winged Teal',
    'cacgoo1': 'Cackling Goose',
    'cacwre': 'Cactus Wren',
    'calqua': 'California Quail',
    'caltow': 'California Towhee',
    'cangoo': 'Canada Goose',
    'canwar': 'Canada Warbler',
    'carchi': 'Carolina Chickadee',
    'carwre': 'Carolina Wren',
    'casfin': "Cassin's Finch", 'caskin': "Cassin's Kingbird", 'caster1': 'Caspian Tern',
    'casvir': "Cassin's Vireo", 'categr': 'Cattle Egret',
    'ccbfin': 'Chestnut-capped Brushfinch',
    'cedwax': 'Cedar Waxwing',
    'chbant1': 'Chestnut-backed Antbird',
    'chbchi': 'Chestnut-backed Chickadee',
    'chbwre1': 'Chestnut-breasted Wren',
    'chcant2': 'Chestnut-crowned Antpitta',
    'chispa': 'Chipping Sparrow',
    'chswar': 'Chestnut-sided Warbler',
    'cinfly2': 'Cinnamon Flycatcher',
    'clanut': "Clark's Nutcracker", 'clcrob': 'Clay-colored Thrush',
    'cliswa': 'Cliff Swallow',
    'cobtan1': 'Common Chlorospingus',
    'cocwoo1': 'Cocoa Woodcreeper',
    'cogdov': 'Common Ground Dove',
    'colcha1': 'Colombian Chachalaca',
    'coltro1': 'Collared Trogon',
    'comgol': 'Common Goldeneye',
    'comgra': 'Common Grackle',
    'comloo': 'Common Loon',
    'commer': 'Common Merganser',
    'compau': 'Common Pauraque',
    'compot1': 'Common Potoo',
    'comrav': 'Common Raven',
    'comyel': 'Common Yellowthroat',
    'coohaw': "Cooper's Hawk", 'cotfly1': 'Common Tody-Flycatcher',
    'cowscj1': 'California Scrub-Jay',
    'cregua1': 'Crested Guan',
    'creoro1': 'Crested Oropendola',
    'crfpar': 'Crimson-fronted Parakeet',
    'cubthr': 'Curve-billed Thrasher',
    'daejun': 'Dark-eyed Junco',
    'dowwoo': 'Downy Woodpecker',
    'ducfly': 'Dusky-capped Flycatcher',
    'dusfly': 'Dusky Flycatcher',
    'easblu': 'Eastern Bluebird',
    'easkin': 'Eastern Kingbird',
    'easmea': 'Eastern Meadowlark',
    'easpho': 'Eastern Phoebe',
    'eastow': 'Eastern Towhee',
    'eawpew': 'Eastern Wood-Pewee',
    'eletro': 'Elegant Trogon',
    'eucdov': 'Eurasian Collared-Dove',
    'eursta': 'European Starling',
    'fepowl': 'Ferruginous Pygmy-Owl',
    'fiespa': 'Field Sparrow',
    'flrtan1': 'Flame-rumped Tanager',
    'foxspa': 'Fox Sparrow',
    'gadwal': 'Gadwall',
    'gamqua': "Gambel's Quail", 'gartro1': 'Gartered Trogon',
    'gbbgul': 'Great Black-backed Gull',
    'gbwwre1': 'Gray-breasted Wood-Wren',
    'gcrwar': 'Golden-crowned Warbler',
    'gilwoo': 'Gila Woodpecker',
    'gnttow': 'Green-tailed Towhee',
    'gnwtea': 'Green-winged Teal',
    'gocfly1': 'Golden-crowned Flycatcher',
    'gockin': 'Golden-crowned Kinglet',
    'gocspa': 'Golden-crowned Sparrow',
    'goftyr1': 'Golden-faced Tyrannulet',
    'gohque1': 'Golden-headed Quetzal',
    'goowoo1': 'Golden-olive Woodpecker',
    'grasal1': 'Grayish Saltator',
    'grbani': 'Groove-billed Ani',
    'grbher3': 'Great Blue Heron',
    'grcfly': 'Great Crested Flycatcher',
    'greegr': 'Great Egret',
    'grekis': 'Great Kiskadee',
    'grepew': 'Greater Pewee',
    'grethr1': 'Great Thrush',
    'gretin1': 'Great Tinamou',
    'greyel': 'Greater Yellowlegs',
    'grhcha1': 'Gray-headed Chachalaca',
    'grhowl': 'Great Horned Owl',
    'grnher': 'Green Heron',
    'grnjay': 'Green Jay',
    'grtgra': 'Great-tailed Grackle',
    'grycat': 'Gray Catbird',
    'gryhaw2': 'Gray Hawk',
    'gwfgoo': 'Greater White-fronted Goose',
    'haiwoo': 'Hairy Woodpecker',
    'heptan': 'Hepatic Tanager',
    'hergul': 'Herring Gull',
    'herthr': 'Hermit Thrush',
    'herwar': 'Hermit Warbler',
    'higmot1': 'Andean Motmot',
    'hofwoo1': "Hoffmann's Woodpecker", 'houfin': 'House Finch',
    'houspa': 'House Sparrow',
    'houwre': 'House Wren',
    'hutvir': "Hutton's Vireo", 'incdov': 'Inca Dove',
    'indbun': 'Indigo Bunting',
    'kebtou1': 'Keel-billed Toucan',
    'killde': 'Killdeer',
    'labwoo': 'Ladder-backed Woodpecker',
    'larspa': 'Lark Sparrow',
    'laufal1': 'Laughing Falcon',
    'laugul': 'Laughing Gull',
    'lazbun': 'Lazuli Bunting',
    'leafly': 'Least Flycatcher',
    'leasan': 'Least Sandpiper',
    'lesgol': 'Lesser Goldfinch',
    'lesgre1': 'Lesser Greenlet',
    'lesvio1': 'Lesser Violetear',
    'linspa': "Lincoln's Sparrow", 'linwoo1': 'Lineated Woodpecker',
    'littin1': 'Little Tinamou',
    'lobdow': 'Long-billed Dowitcher',
    'lobgna5': 'Long-billed Gnatwren',
    'logshr': 'Loggerhead Shrike',
    'lotduc': 'Long-tailed Duck',
    'lotman1': 'Long-tailed Manakin',
    'lucwar': "Lucy's Warbler", 'macwar': "MacGillivray's Warbler", 'magwar': 'Magnolia Warbler',
    'mallar3': 'Mallard',
    'marwre': 'Marsh Wren',
    'mastro1': 'Masked Trogon',
    'meapar': 'Mealy Parrot',
    'melbla1': 'Melodious Blackbird',
    'monoro1': 'Montezuma Oropendola',
    'mouchi': 'Mountain Chickadee',
    'moudov': 'Mourning Dove',
    'mouela1': 'Mountain Elaenia',
    'mouqua': 'Mountain Quail',
    'mouwar': 'Mourning Warbler',
    'mutswa': 'Mute Swan',
    'naswar': 'Nashville Warbler',
    'norcar': 'Northern Cardinal',
    'norfli': 'Northern Flicker',
    'normoc': 'Northern Mockingbird',
    'norpar': 'Northern Parula',
    'norsho': 'Northern Shoveler',
    'norwat': 'Northern Waterthrush',
    'nrwswa': 'Northern Rough-winged Swallow',
    'nutwoo': "Nuttall's Woodpecker", 'oaktit': 'Oak Titmouse',
    'obnthr1': 'Orange-billed Nightingale-Thrush',
    'ocbfly1': 'Ochre-bellied Flycatcher',
    'oliwoo1': 'Olivaceous Woodcreeper',
    'olsfly': 'Olive-sided Flycatcher',
    'orbeup1': 'Orange-bellied Euphonia',
    'orbspa1': 'Orange-billed Sparrow',
    'orcpar': 'Orange-chinned Parakeet',
    'orcwar': 'Orange-crowned Warbler',
    'orfpar': 'Orange-fronted Parakeet',
    'osprey': 'Osprey',
    'ovenbi1': 'Ovenbird',
    'pabspi1': 'Pale-breasted Spinetail',
    'paltan1': 'Palm Tanager',
    'palwar': 'Palm Warbler',
    'pasfly': 'Pacific-slope Flycatcher',
    'pavpig2': 'Pale-vented Pigeon',
    'phivir': 'Philadelphia Vireo',
    'pibgre': 'Pied-billed Grebe',
    'pilwoo': 'Pileated Woodpecker',
    'pinsis': 'Pine Siskin',
    'pirfly1': 'Piratic Flycatcher',
    'plawre1': "Cabanis's Wren", 'plaxen1': 'Plain Xenops',
    'plsvir': 'Plumbeous Vireo',
    'plupig2': 'Plumbeous Pigeon',
    'prowar': 'Prothonotary Warbler',
    'purfin': 'Purple Finch',
    'purgal2': 'Purple Gallinule',
    'putfru1': 'Purple-throated Fruitcrow',
    'pygnut': 'Pygmy Nuthatch',
    'rawwre1': 'Rufous-and-white Wren',
    'rcatan1': 'Red-crowned Ant-Tanager',
    'rebnut': 'Red-breasted Nuthatch',
    'rebsap': 'Red-breasted Sapsucker',
    'rebwoo': 'Red-bellied Woodpecker',
    'redcro': 'Red Crossbill',
    'reevir1': 'Red-eyed Vireo',
    'rehbar1': 'Red-headed Barbet',
    'relpar': 'Red-lored Parrot',
    'reshaw': 'Red-shouldered Hawk',
    'rethaw': 'Red-tailed Hawk',
    'rewbla': 'Red-winged Blackbird',
    'ribgul': 'Ring-billed Gull',
    'rinkin1': 'Ringed Kingfisher',
    'roahaw': 'Roadside Hawk',
    'robgro': 'Rose-breasted Grosbeak',
    'rocpig': 'Rock Pigeon',
    'rotbec': 'Rose-throated Becard',
    'royter1': 'Royal Tern',
    'rthhum': 'Ruby-throated Hummingbird',
    'rtlhum': 'Rufous-tailed Hummingbird',
    'ruboro1': 'Russet-backed Oropendola',
    'rubpep1': 'Rufous-browed Peppershrike',
    'rubrob': 'Rufous-backed Robin',
    'rubwre1': 'Rufous-breasted Wren',
    'ruckin': 'Ruby-crowned Kinglet',
    'rucspa1': 'Rufous-collared Sparrow',
    'rucwar': 'Rufous-capped Warbler',
    'rucwar1': 'Russet-crowned Warbler',
    'rudpig': 'Ruddy Pigeon',
    'rudtur': 'Ruddy Turnstone',
    'rufhum': 'Rufous Hummingbird',
    'rugdov': 'Ruddy Ground Dove',
    'rumfly1': 'Rusty-margined Flycatcher',
    'runwre1': 'Rufous-naped Wren',
    'rutjac1': 'Rufous-tailed Jacamar',
    'saffin': 'Saffron Finch',
    'sancra': 'Sandhill Crane',
    'sander': 'Sanderling',
    'savspa': 'Savannah Sparrow',
    'saypho': "Say's Phoebe", 'scamac1': 'Scarlet Macaw',
    'scatan': 'Scarlet Tanager',
    'scbwre1': 'Scaly-breasted Wren',
    'scptyr1': 'Scale-crested Pygmy-Tyrant',
    'scrtan1': 'Scrub Tanager',
    'semplo': 'Semipalmated Plover',
    'shicow': 'Shiny Cowbird',
    'sibtan2': 'Silver-beaked Tanager',
    'sinwre1': 'Sinaloa Wren',
    'sltred': 'Slate-throated Redstart',
    'smbani': 'Smooth-billed Ani',
    'snogoo': 'Snow Goose',
    'sobtyr1': 'Southern Beardless-Tyrannulet',
    'socfly1': 'Social Flycatcher',
    'solsan': 'Solitary Sandpiper',
    'sonspa': 'Song Sparrow',
    'soulap1': 'Southern Lapwing',
    'sposan': 'Spotted Sandpiper',
    'spotow': 'Spotted Towhee',
    'spvear1': 'Sparkling Violetear',
    'squcuc1': 'Squirrel Cuckoo',
    'stbori': 'Streak-backed Oriole',
    'stejay': "Steller's Jay", 'sthant1': 'Streak-headed Antbird',
    'sthwoo1': 'Streak-headed Woodcreeper',
    'strcuc1': 'Striped Cuckoo',
    'strfly1': 'Streaked Flycatcher',
    'strsal1': 'Streaked Saltator',
    'stvhum2': 'Steely-vented Hummingbird',
    'subfly': 'Sulphur-bellied Flycatcher',
    'sumtan': 'Summer Tanager',
    'swaspa': 'Swamp Sparrow',
    'swathr': "Swainson's Thrush", 'tenwar': 'Tennessee Warbler',
    'thbeup1': 'Thick-billed Euphonia',
    'thbkin': 'Thick-billed Kingbird',
    'thswar1': 'Three-striped Warbler',
    'towsol': "Townsend's Solitaire", 'treswa': 'Tree Swallow',
    'trogna1': 'Tropical Gnatcatcher',
    'trokin': 'Tropical Kingbird',
    'tromoc': 'Tropical Mockingbird',
    'tropar': 'Tropical Parula',
    'tropew1': 'Tropical Pewee',
    'tuftit': 'Tufted Titmouse',
    'tunswa': 'Tundra Swan',
    'veery': 'Veery',
    'verdin': 'Verdin',
    'vigswa': 'Violet-green Swallow',
    'warvir': 'Warbling Vireo',
    'wbwwre1': 'White-breasted Wood-Wren',
    'webwoo1': 'Wedge-billed Woodcreeper',
    'wegspa1': 'White-eared Ground-Sparrow',
    'wesant1': 'Black-crowned Antshrike',
    'wesblu': 'Western Bluebird',
    'weskin': 'Western Kingbird',
    'wesmea': 'Western Meadowlark',
    'westan': 'Western Tanager',
    'wewpew': 'Western Wood-Pewee',
    'whbman1': 'White-bearded Manakin',
    'whbnut': 'White-breasted Nuthatch',
    'whcpar': 'White-crowned Parrot',
    'whcsee1': "Morelet's Seedeater", 'whcspa': 'White-crowned Sparrow',
    'whevir': 'White-eyed Vireo',
    'whfpar1': 'White-fronted Parrot',
    'whimbr': 'Whimbrel',
    'whiwre1': 'Whiskered Wren',
    'whtdov': 'White-tipped Dove',
    'whtspa': 'White-throated Sparrow',
    'whwbec1': 'White-winged Becard',
    'whwdov': 'White-winged Dove',
    'wilfly': 'Willow Flycatcher',
    'willet1': 'Willet',
    'wilsni1': "Wilson's Snipe", 'wiltur': 'Wild Turkey',
    'wlswar': "Wilson's Warbler", 'wooduc': 'Wood Duck',
    'woothr': 'Wood Thrush',
    'wrenti': 'Wrentit',
    'y00475': 'American Coot',
    'yebcha': 'Yellow-breasted Chat',
    'yebela1': 'Yellow-bellied Elaenia',
    'yebfly': 'Yellow-bellied Flycatcher',
    'yebori1': 'Yellow-backed Oriole',
    'yebsap': 'Yellow-bellied Sapsucker',
    'yebsee1': 'Yellow-bellied Seedeater',
    'yefgra1': 'Yellow-faced Grassquit',
    'yegvir': 'Yellow-green Vireo',
    'yehbla': 'Yellow-headed Blackbird',
    'yehcar1': 'Yellow-headed Caracara',
    'yelgro': 'Yellow Grosbeak',
    'yelwar': 'Yellow Warbler',
    'yeofly1': 'Yellow-olive Flycatcher',
    'yerwar': 'Yellow-rumped Warbler',
    'yeteup1': 'Yellow-throated Euphonia',
    'yetvir': 'Yellow-throated Vireo'
}

INV_EBIRD_LABEL = {v: k for k, v in EBIRD_LABEL.items()}