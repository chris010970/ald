import os
import re
import fnmatch

def getFileList ( path, pattern ):

    """
    Placeholder
    """

    # get pattern matched file list
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            x = re.search( pattern, name )
            if x is not None:                
                result.append( os.path.join(root, name) )

    return result


def getPathList ( path, pattern ):

    """
    Placeholder
    """

    # get pattern matched sub-folder list
    result = []
    for root, dirs, files in os.walk(path):

        x = re.search( pattern, root )
        if x is not None:
            result.append( root )

    return result


def getFile ( path, pattern ):

    """
    Placeholder
    """

    # get uniquely named file in path
    result = None
    filelist = getFileList( path, pattern )

    if len ( filelist ) == 1:
        result = filelist[ 0 ]

    return result


def getPath ( path, pattern ):

    """
    Placeholder
    """

    # get uniquely named file in path
    result = None
    pathlist = getPathList( path, pattern )

    if len ( pathlist ) == 1:
        result = pathlist[ 0 ]

    return result


def removeFileList( filelist ):

    """
    Placeholder
    """

    # remove file list
    for pathname in filelist:
        if os.path.exists( pathname ):
            os.remove( pathname )

    return

