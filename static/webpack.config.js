const webpack = require("webpack");
const path = require('path');
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const config = {
    entry: __dirname + '/js/index.jsx',
    output:{
        path: __dirname + "/dist",
        filename:'bundle.js'

    },
    module: {
        rules:[
           { test:/\.jsx?/,exclude:/node_modules/,use:'babel-loader'},
           {
                test:/\.css$/, use: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: "css-loader"
        })
                        }
        ]
    },
    resolve:{
        extensions:['.js','.jsx','.css']
    },
    plugins: [
    new ExtractTextPlugin("styles.css"),
  ]

};

module.exports = config;