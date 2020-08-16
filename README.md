# Offload Your Static Content to s3

The code is used in [this article](https://netrewrite.com/posts/offload-static-content-amazon-s3/).

Your website has probably tons of static files. And for some reason 
you want those files to be copied over to an **s3** bucket. 

If you run `detect-changes.py` (preferably via cron), it will track the static 
files in your website and if changes are detected it will subsequently run `s3-sync.sh` 
which will synchronize your website with your **s3** bucket 
(only the files you specify).

You just need to specify the paths to your folders/files in the scripts. Needless to say 
if placed in `~/.local/bin` you can ditch the scripts' extensions and use them as 
shell commands too.
