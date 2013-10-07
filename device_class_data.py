supported_devices = [
[1,1,0],
[1,2,0],
[2,2,1],
[2,3,0xff],
[2,6,0],
[3,0,0],
[6,1,1],
[7,1,2],
[8,6,0x50],
[9,0,0],
[0x0a,0,0],
[0x0b,0,0]
]

device_class_list = [
["Audio", 1],
["CDC Control", 2],
["Human Interface Device", 3],
#5 physical
["Image", 6],
["Printer", 7],
["Mass Storage", 8],
["Hub", 9],
["CDC Data", 10],
["Smart Card", 11],
["Content Security", 13],
["Video", 14],
["Personal Healthcare", 15],
# Diagnostic devices
# Wireless controller
["Application specific", 254]
]

device_subclass_list = [
[1, "Sub-class undefined", 0],
[1, "Audio control", 1],
[1, "Audio streaming", 2],
[1, "Midi streaming", 3],
[2, "Direct Line Control Model", 1],
[2, "Abstract Control Model", 2],
[2, "Telephone Control Model", 3],
[2, "Multi-Channel Control Model", 4],
[2, "CAPI Control Model", 5],
[2, "Ethernet Networking Control Model", 6],
[2, "ATM Networking Control Model", 7],
[2, "Wireless Handset Control Model", 8],
[2, "Device Management", 9],
[2, "Mobile Direct Line Model", 10],
[2, "OBEX", 11],
[2, "Ethernet Emulation Model", 12],
[2, "Network Control Model", 13],
[3, "No subclass", 0],
[3, "Boot interface", 1],
[6, "Still image capture device", 1],
[7, "Default", 1],
[8, "De facto use", 0],
[8, "RPC", 1],
[8, "MMC-5 (ATAPI)", 2],
[8, "QIC-157 (obsolete)", 3],
[8, "UFI", 4],
[8, "SFF-8070i (obsolete)", 5],
[8, "SCSI", 6],
[8, "LSD FS", 7],
[8, "IEE 1667", 8],
[8, "Vendor specific", 255],
[9, "Default", 0],
[10, "Default", 0],
[11, "Default", 0],
[13, "Default", 0],
[14, "Undefined", 0],
[14, "Video Control", 1],
[14, "Video streaming", 2],
[14, "Video Interface Collection", 3],
[15, "Default", 0],
[254, "DFU: Upgrade code", 1],
[254, "IrDA Bridge", 2],
[254, "Test and Measurement", 3]
]


device_protocol_list = [
[1, "PR Protocol undefined", 0],
[2, "No class-specific protocol required", 0],
[2, "AT commands V.250", 1],
[2, "AT commands specified by PCCA-101", 2],
[2, "AT commands specified by PCCA-101 and Annex O", 3],
[2, "AT commands specified by GSM 07.07", 4],
[2, "AT commands specified by 3GPP 27.007", 5],
[2, "AT commands specified by TIA for CDMA", 6],
[2, "Ethernet Emulation Model", 7],
[2, "External protocol", 254],
[2, "Vendor specific", 255],
[3, "None", 0],
[3, "Keyboard", 1],
[3, "Mouse", 2],
[6, "Bulk-only protocol", 1],
[7, "Unidirectional interface", 1],
[7, "Bidirectional interface", 2],
[7, "1284.4 compatible bi-directional interface", 3],
[7, "Vendor specific", 255],
[8, "CBI with command completion interrupt", 0],
[8, "CBI without command completion interrupt", 1],
[8, "Obsolete", 2],
[8, "BBB", 80],
[8, "UAS", 98],
[8, "Vendor specific", 255],
[9, "Default", 0],
[10, "Default", 0],
[10, "Network Transfer Block", 1],
[10, "ISDN BRI physical interface protocol", 48],
[10, "HDLC", 49],
[10, "Transparent", 50],
[10, "Q.921 management protocol", 80],
[10, "Q.921 data link protocol", 81],
[10, "Q.921 TEI-multiplexor", 82],
[10, "V.42bis", 144],
[10, "Q.931/Euro-ISDN", 145],
[10, "V.120", 146],
[10, "CAPI2.0", 147],
[10, "Host based driver", 253],
[10, "Protocol unit functional descriptor", 254],
[10, "Vendor specific", 255],
[11, "Default", 0],
[13, "Default", 0],
[14, "Undefined", 0],
[14, "Protocol 15", 1],
[15, "Default", 0],
[254, "DFU: Runtime protocol", 1],
[254, "IrDA Bridge", 0],
[254, "Test and Measurement: default", 0],
[254, "Test and Measurement: USB488 interface", 1]

]

