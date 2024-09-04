from pyais import IterMessages

fake_stream = [
    b"!AIVDM,1,1,,A,13HOI:0P0000VOHLCnHQKwvL05Ip,0*23",
    b"!AIVDM,1,1,,A,133sVfPP00PD>hRMDH@jNOvN20S8,0*7F",
    b"!AIVDM,1,1,,B,100h00PP0@PHFV`Mg5gTH?vNPUIp,0*3B",
    b"!AIVDM,1,1,,B,13eaJF0P00Qd388Eew6aagvH85Ip,0*45",
    b"!AIVDM,1,1,,A,14eGrSPP00ncMJTO5C6aBwvP2D0?,0*7A",
    b"!AIVDM,1,1,,A,15MrVH0000KH<:V:NtBLoqFP2H9:,0*2F",
]
for msg in IterMessages(fake_stream):
    print(msg.decode())