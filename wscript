srcdir = "."
blddir = "build"
VERSION = "0.0.1"

def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")
  conf.env.append_value("LIBPATH", "/Applications/VLC.app/Contents/MacOS/lib")
  conf.env.append_value("LIB", "vlc.5")
   
def build(bld):
  obj = bld.new_task_gen("cxx", "shlib", "node_addon")
  obj.cxxflags = ["-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-I/Applications/VLC.app/Contents/MacOS/include"]
  obj.target = "naudio"
  obj.source = "naudio.cc"
