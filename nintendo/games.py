
#===== Wii U Games =====#

class Friends:
	TITLE_ID_EUR = 0x10001C00
	TITLE_ID_USA = 0x10001C00
	TITLE_ID_JAP = 0x10001C00
	LATEST_VERSION = 0
	
	GAME_SERVER_ID = 0x3200
	ACCESS_KEY = "ridfebb9"
	NEX_VERSION = 20000

class DKCTF:
	TITLE_ID_EUR = 0x0005000010138300
	TITLE_ID_USA = 0x0005000010137F00
	TITLE_ID_JAP = 0x0005000010144800
	LATEST_VERSION = 17
	
	GAME_SERVER_ID = 0x10144800
	ACCESS_KEY = "7fcf384a"
	NEX_VERSION = 30400 #3.4.0
	SERVER_VERSION = 3
	
class Minecraft:
	TITLE_ID_EUR = 0x00050000101D7500
	TITLE_ID_USA = 0x00050000101D9D00
	TITLE_ID_JAP = 0x00050000101DBE00
	LATEST_VERSION = 688
	
	GAME_SERVER_ID = 0x101D9D00
	ACCESS_KEY = "f1b61c8e"
	NEX_VERSION = 30901 #3.9.1
	
class MK8:
	TITLE_ID_EUR = 0x000500001010ED00
	TITLE_ID_USA = 0x000500001010EC00
	TITLE_ID_JAP = 0x000500001010EB00
	LATEST_VERSION = 64
	
	GAME_SERVER_ID = 0x1010EB00
	ACCESS_KEY = "25dbf96a"
	NEX_VERSION = 30504 #3.5.4 (AMK patch)
	SERVER_VERSION = 2002
	
class PokkenTournament:
	TITLE_ID_EUR = 0x00050000101DF400
	TITLE_ID_USA = 0x00050000101DF500
	TITLE_ID_JAP = 0x00050000101C5800
	LATEST_VERSION = 64
	
	GAME_SERVER_ID = 0x101C5800
	ACCESS_KEY = "6ef3adf1"
	NEX_VERSION = 31000
	
class Puddle:
	TITLE_ID_EUR = 0x000500001010FB00
	TITLE_ID_USA = 0x0005000010110500
	LATEST_VERSION = 16
	
	GAME_SERVER_ID = 0x1010FB00
	ACCESS_KEY = "afcffb5c"
	NEX_VERSION = 30001 #3.0.1.4
	
class SMM:
	TITLE_ID_EUR = 0x000500001018DD00
	TITLE_ID_USA = 0x000500001018DC00
	TITLE_ID_JAP = 0x000500001018DB00
	LATEST_VERSION = 272
	
	GAME_SERVER_ID = 0x1018DB00
	ACCESS_KEY = "9f2b4678"
	NEX_VERSION = 30810 #3.8.10 (AMA patch)
	SERVER_VERSION = 3017
	

#===== Switch Games =====#

class ACNH:
	TITLE_ID = 0x01006F8002326000
	TITLE_VERSION = 0x70000
	
	GAME_SERVER_ID = 0x2EE2E300
	ACCESS_KEY = "v43a10em"
	NEX_VERSION = 40603 #4.6.3
	CLIENT_VERSION = 2

class CaveStory:
	GAME_SERVER_ID = 0x2BA73000
	ACCESS_KEY = "c2a631ad"
	NEX_VERSION = 40003 #4.0.3
	
class DQBuilders:
	GAME_SERVER_ID = 0x2CD9DB00
	ACCESS_KEY = "e720a303"
	NEX_VERSION = 40003 #4.0.3

class LM3:
	GAME_SERVER_ID = 0x20DE2100
	ACCESS_KEY = "aab95246"
	NEX_VERSION = 40600 #4.6.2
	CLIENT_VERSION = 2

class MK8Deluxe:
	GAME_SERVER_ID = 0x2B309E01
	ACCESS_KEY = "09c1c475"
	NEX_VERSION = 40302 #4.3.2 (apptrbs)
	SERVER_VERSION = 4011
	
	PIA_VERSION = 50604

class SMM2:
	TITLE_ID = 0x01009B90006DC000
	TITLE_VERSION = 0x40000
	
	GAME_SERVER_ID = 0x22306D00
	ACCESS_KEY = "fdf6617f"
	NEX_VERSION = 40605 #4.6.18 (appslop)
	CLIENT_VERSION = 60
	
	PIA_VERSION = 51800
	PIA_APP_VERSION = 3
	PIA_KEY = bytes.fromhex("667c18475889faab61f93ef1da180971")

class SMO:
	GAME_SERVER_ID = 0x255BA201
	ACCESS_KEY = "afef0ecf"
	NEX_VERSION = 40302 #4.3.2
	
class Splatoon2:
	GAME_SERVER_ID = 0x2DF33D01
	ACCESS_KEY = "4eb18d39"
	NEX_VERSION = 40308 #4.3.8 (appblz)
	
	PIA_VERSION = 50901
	PIA_APP_VERSION = 60
	PIA_KEY = bytes.fromhex("ee182a63e216cdb1f51ad4bed8cf6508")
	
class Tetris99:
	TITLE_ID = 0x010040600C5CE000
	TITLE_VERSION = 0x50000
	
	GAME_SERVER_ID = 0x23BDA200
	ACCESS_KEY = "cdd6114d"
	NEX_VERSION = 40600 #4.6.4 (app99)
	CLIENT_VERSION = 5
