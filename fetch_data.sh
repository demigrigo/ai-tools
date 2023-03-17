# bin/bash

rm main.zip
rm -rf ./data
wget https://github.com/Auden-Musulin-Papers/amp-data/archive/refs/heads/entities.zip
unzip entities
mv amp-data-entities/data ./data
rm -rf amp-data-entities
rm entities.zip

rm -rf ./data/tmp
rm -rf ./data/images
rm -rf ./data/meta
rm -rf ./data/ric_metadata
rm ./data/imprint.xml