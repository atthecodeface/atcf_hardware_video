import cdl_desc
from cdl_desc import CdlModule, CModel

class TeletextModules(cdl_desc.Modules):
    name = "teletext"
    c_src_dir   = "cmodel"
    src_dir     = "cdl"
    tb_src_dir  = "tb_cdl"
    include_dir = "cdl"
    libraries = ["apb", "std"]
    modules = []
    # saa5050 needs t_bbc_micro_sram_request
    # modules += [ CdlModule("saa5050") ]
    modules += [ CdlModule("teletext",constants={"flashing_on_count":10,"max_flashing_count":40}) ]
    pass

class FramebufferTimingCdl(CdlModule):
    """
    timing_width is the log2 of the max clock ticks per line - needs to be at least 12 for 2k pixels wide
    """
    constants = {"timing_width":12}

class FramebufferTeletextCdl(CdlModule):
    """
    Note that framebufferteletext uses two consecutive CSR select values X and X|1
    csr_select_default is the default value for the CSR select as a target
        If the csr_select_in value is tied low then csr_select will always be csr_select_default
        So this permits hard-wiring of the CSR select values
    cfg_downsize_x is 1 if characters should be displayed at half width; else all pixel columns are displayed
    cfg_downsize_y is 1 if characters should be displayed at half height; else all pixel rows are displayed

    An old-fashioned teletext screen was 625 lines interlaced, 64us per displayed line
    With 40x25 teletext characters (12x20 pixels each) this mean 480x500 pixels on a screen, but interlaced
    To keep an approximately square aspect ratio starting with 12x20 requires skipping alternate y; hence
    for a standard screen display cfg_downsize_y is 1, cfg_downsize_x is 0
    """
    constants = {"csr_select_default":0,
                 "cfg_downsize_x":0,
                 "cfg_downsize_y":1}

class FramebufferModules(cdl_desc.Modules):
    name = "framebuffer"
    c_src_dir   = "cmodel"
    src_dir     = "cdl"
    tb_src_dir  = "tb_cdl"
    include_dir = "cdl"
    libraries = ["apb", "std"]
    modules = []
    modules += [ FramebufferTimingCdl("framebuffer_timing") ]
    modules += [ FramebufferTeletextCdl("framebuffer_teletext") ]
    modules += [ CdlModule("framebuffer") ]
    pass

modules=cdl_desc.Modules.__subclasses__
