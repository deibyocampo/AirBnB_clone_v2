#!/usr/bin/python3

""" script will generate a .tgz archive from web_static """

from fabric.api import *
from datetime import datetime
import os.path


env.hosts = ['35.243.213.140', '34.73.54.82']
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"


def do_pack():
    """
    function will convert the file into the .tgz format
    running on local for contents in web_static
    """
    local("mkdir -p versions")
    cur_time = datetime.now().strftime("%Y%m%d%H%M%S")
    arch_name = "versions/web_static_{}.tgz".format(cur_time)
    tgz_vert = local("tar -cvzf {} web_static".format(arch_name))

    if tgz_vert.succeeded:
        return arch_name
    else:
        return None


def do_deploy(archive_path):
    ''' distributes an archive to web server '''
    filename = archive_path.split('/')[-1]
    archivefile = filename.split('.')[0]
    archivefolder = ("/data/web_static/releases/{}".format(archivefile))

    try:
        put(archive_path, "tmp/{}".format(filename))
        run("mkdir -p {}".format(archivefolder))
        run("tar -xzf /tmp/{} -C {}".format(filename, archivefolder))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}".format(archivefolder, archivefolder))
        run("rm -rf {}/web_static/".format(archivefolder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(archivefolder))
        return True
    except:
        return False
