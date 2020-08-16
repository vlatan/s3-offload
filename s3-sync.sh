#!/bin/sh

# find out the aws path with 'which aws' in your terminal
aws='/usr/local/bin/aws'

# your s3 bucket
bucket='s3://your-bucket'

# get into the website's root folder
cd /var/www/example.com/htdocs

echo "Syncing htdocs (static files) with $bucket..."

# sync images(jpg, jpeg, png, gif, svg), css and js to $bucket
$aws s3 sync . $bucket --exclude "*" --include "*.jpg" \
--include "*.jpeg" --include "*.png" --include "*.gif" \
--include "*.svg" --include "*.css" --include "*.js" \
--cache-control "public, max-age=31536000" \
--storage-class INTELLIGENT_TIERING \
--acl public-read --delete --quiet

# sync json, ico and xml to $bucket with less max-age
$aws s3 sync . $bucket --exclude "*" --include "*.json" \
--include "*.ico" --include ".xml" \
--cache-control "public, max-age=86400" \
--storage-class INTELLIGENT_TIERING \
--acl public-read --delete --quiet

now=$(date + "%D - %T")
echo "Static files synced. Current time: $now.\n"
