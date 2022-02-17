from pyisemail import is_email

# test
def check_mails(mails):
    valid_mails = []
    for mail in mails:
        if check_mail_address(mail):
            valid_mails.append(mail)
    return valid_mails


def check_mail_address(mail):
    # from email_validator import validate_email, EmailNotValidError
    # alternatives  exist email_validator etc. but if wanto to use on premiss module is not gurantied if  important mail address is exist we can validate it options using api or used more pofisticated modules forexample check mx records etc.
    img_exts = ["ase", "art", "bmp", "blp", "cd5", "cit", "cpt", "cr2", "cut", "dds", "dib", "djvu", "egt", "exif",
                "gif", "gpl", "grf", "icns", "ico", "iff", "jng", "jpeg", "jpg", "jfif", "jp2", "jps", "lbm", "max",
                "miff", "mng", "msp", "nef", "nitf", "ota", "pbm", "pc1", "pc2", "pc3", "pcf", "pcx", "pdn", "pgm",
                "PI1", "PI2", "PI3", "pict", "pct", "pnm", "pns", "ppm", "psb", "psd", "pdd", "psp", "px", "pxm", "pxr",
                "qfx", "raw", "rle", "sct", "sgi", "rgb", "int", "bw", "tga", "tiff", "tif", "vtf", "xbm", "xcf", "xpm",
                "3dv", "amf", "ai", "awg", "cgm", "cdr", "cmx", "dxf", "e2d", "egt", "eps", "fs", "gbr", "odg", "svg",
                "stl", "vrml", "x3d", "sxd", "v2d", "vnd", "wmf", "emf", "art", "xar", "png", "webp", "jxr", "hdp",
                "wdp", "cur", "ecw", "iff", "lbm", "liff", "nrrd", "pam", "pcx", "pgf", "sgi", "rgb", "rgba", "bw",
                "int", "inta", "sid", "ras", "sun", "tga", "heic", "heif"]
    try:
        if is_email(mail):
            mail = mail.split("@")
            l = mail[1].count('.')
            if l == 0:
                if mail[1] in img_exts:
                    return False
                else:
                    return True
            elif l == 1:

                endfix = mail[1].split('.')
                if endfix[1] in img_exts:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False
    except:
        return False
