#!/astro/apps/pkg/python64/bin/python
import os
import sys

SPREFIX_ROOT = '/astro/users/joshsohi/sprefix'

def abspath(path):
 return os.path.abspath(path)

def link_unlink(link=True): 
 for dirpath, dirnames, filenames in os.walk('.', topdown=link):
  for dirname in dirnames:
   sp_dir = abspath(os.path.join(SPREFIX_ROOT, dirpath, dirname))
   if link:
    try:
     os.mkdir(sp_dir)
    except:
     pass
   else:
    try:
     os.rmdir(sp_dir)
    except:
     pass
   
  for filename in filenames:
   fpath = abspath(os.path.join(dirpath, filename))
   lpath = abspath(os.path.join(SPREFIX_ROOT, dirpath, filename))
   if link:
    _link(fpath, lpath)
   else:
    _unlink(fpath, lpath)
    
def _link(fpath, lpath):
 if os.path.exists(lpath):pass
  #print 'Existing Link: {0}-->{1}'.format(os.readlink(lpath), lpath)
  #print 'Will Not Link: {0}-->{1}'.format(fpath, lpath)
 else:
  if os.path.lexists(lpath):
   os.remove(lpath)
  os.symlink(fpath, lpath)
  print 'Linked: {0}-->{1}'.format(fpath, lpath)

def _unlink(fpath, lpath):
 if os.path.lexists(lpath) and os.path.isfile(lpath):
  f_lpath = os.readlink(lpath)
  if f_lpath == fpath:
   os.remove(lpath)
   print 'Unlinked: {0}-->{1}'.format(f_lpath, lpath)

def clean():
 sprefix_root_abs = abspath(SPREFIX_ROOT)
 for dirpath, dirnames, filenames in os.walk(SPREFIX_ROOT, topdown=True):
  for dirname in dirnames:
   sp_dir = abspath(os.path.join(SPREFIX_ROOT, dirpath, dirname))
   try:
    os.rmdir(sp_dir)
   except:
    pass 
  for filename in filenames:
   lpath = abspath(os.path.join(SPREFIX_ROOT, dirpath, filename))
   if (os.path.lexists(lpath) and not os.path.exists(lpath)) or not os.path.islink(lpath):
    os.remove(lpath)
    print 'Removed: {0}'.format(lpath)

def usage():pass

def Main():
 try: action = sys.argv[1]
 except: action = 'link'
 
 if action == 'link':
  link_unlink()
 elif action == 'unlink':
  link_unlink(False)
 elif action == 'clean':
  clean()
 else:
  usage()


if __name__ == '__main__': Main()




