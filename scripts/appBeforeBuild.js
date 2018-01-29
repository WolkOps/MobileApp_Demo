#!/usr/bin/env node

module.exports = function(context) {
  var fs = require('fs');
  var path = require('path');
  var fileToCopy = "scripts/build-extras.gradle"
  var rootdir = context.opts.projectRoot;
  var srcfile = path.join(rootdir, fileToCopy);
  var destfile = path.join(rootdir, "platforms/android/app/build-extras.gradle");

  var destdir = path.dirname(destfile);
  if (fs.existsSync(srcfile) && fs.existsSync(destdir)) {
    fs.createReadStream(srcfile).pipe(
      fs.createWriteStream(destfile));
  }

}