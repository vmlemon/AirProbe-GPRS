# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gsm', [dirname(__file__)])
        except ImportError:
            import _gsm
            return _gsm
        if fp is not None:
            try:
                _mod = imp.load_module('_gsm', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gsm = swig_import_helper()
    del swig_import_helper
else:
    import _gsm
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class gsm_run_bb_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gsm_run_bb)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> gsm_run_bb_sptr
        __init__(self,  p) -> gsm_run_bb_sptr
        """
        this = _gsm.new_gsm_run_bb_sptr(*args)
        try: self.this.append(this)
        except: self.this = this
    def __deref__(self):
        """__deref__(self)"""
        return _gsm.gsm_run_bb_sptr___deref__(self)

    __swig_destroy__ = _gsm.delete_gsm_run_bb_sptr
    __del__ = lambda self : None;
    def history(self):
        """history(self) -> unsigned int"""
        return _gsm.gsm_run_bb_sptr_history(self)

    def output_multiple(self):
        """output_multiple(self) -> int"""
        return _gsm.gsm_run_bb_sptr_output_multiple(self)

    def relative_rate(self):
        """relative_rate(self) -> double"""
        return _gsm.gsm_run_bb_sptr_relative_rate(self)

    def start(self):
        """start(self) -> bool"""
        return _gsm.gsm_run_bb_sptr_start(self)

    def stop(self):
        """stop(self) -> bool"""
        return _gsm.gsm_run_bb_sptr_stop(self)

    def nitems_read(self, *args):
        """nitems_read(self, unsigned int which_input) -> uint64_t"""
        return _gsm.gsm_run_bb_sptr_nitems_read(self, *args)

    def nitems_written(self, *args):
        """nitems_written(self, unsigned int which_output) -> uint64_t"""
        return _gsm.gsm_run_bb_sptr_nitems_written(self, *args)

    def detail(self):
        """detail(self) -> gr_block_detail_sptr"""
        return _gsm.gsm_run_bb_sptr_detail(self)

    def set_detail(self, *args):
        """set_detail(self, gr_block_detail_sptr detail)"""
        return _gsm.gsm_run_bb_sptr_set_detail(self, *args)

    def name(self):
        """name(self) -> string"""
        return _gsm.gsm_run_bb_sptr_name(self)

    def input_signature(self):
        """input_signature(self) -> gr_io_signature_sptr"""
        return _gsm.gsm_run_bb_sptr_input_signature(self)

    def output_signature(self):
        """output_signature(self) -> gr_io_signature_sptr"""
        return _gsm.gsm_run_bb_sptr_output_signature(self)

    def unique_id(self):
        """unique_id(self) -> long"""
        return _gsm.gsm_run_bb_sptr_unique_id(self)

    def to_basic_block(self):
        """to_basic_block(self) -> gr_basic_block_sptr"""
        return _gsm.gsm_run_bb_sptr_to_basic_block(self)

    def check_topology(self, *args):
        """check_topology(self, int ninputs, int noutputs) -> bool"""
        return _gsm.gsm_run_bb_sptr_check_topology(self, *args)

gsm_run_bb_sptr_swigregister = _gsm.gsm_run_bb_sptr_swigregister
gsm_run_bb_sptr_swigregister(gsm_run_bb_sptr)

gsm_run_bb_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id ())


def run_bb():
  """run_bb() -> gsm_run_bb_sptr"""
  return _gsm.run_bb()


