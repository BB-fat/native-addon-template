const {
    add,
} = require('node-gyp-build')(__dirname);

module.exports = {
    add: (a, b) => new Promise(resolve => resolve(add(a, b))),
    addSync: add,
};
