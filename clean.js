const config = {
    num: 20,
    listName: '我喜欢的音乐',
}

var es = function (name) {
    return document.getElementsByClassName(name)
}

var e = function (id) {
    return document.getElementById(id)
}

var sleep = function (d) {
    for (var t = Date.now(); Date.now() - t <= d;) ;
}


var removeElement = function (name) {
    name.parentNode.removeChild(name)
}

var collectSong = function (index) {
    var e = es(' s-fc3')[index]
    e.getElementsByClassName('icn icn-fav')[0].click()
}

var chooseList = function (index) {
    if (es('xtag ').length == 0) {
        var c1 = es('m-layer z-show m-layer-w5')[0]
        var c2 = es('m-layer z-show m-layer-w2')[0]
        if (c1 != undefined) {
            removeElement(c1)
        } else {
            removeElement(c2)
        }
    } else {
        es('xtag ')[index].click()
    }
}

var splitList = function (numOfSongs) {
    var n = numOfSongs
    var index = 1
    for (var i = 2; i <= n; i++) {
        collectSong(i)
        chooseList(index)
        if (i % config.num == 0) {
            index += 1
        }
    }
}

var numOfSongs = function () {
    var n = document.getElementById('flag_trackCount').textContent
    return Number(n)
}

var createList = function (name) {
    es('u-btn u-btn-crt f-fr j-flag')[0].click()
    if (es('u-txt j-flag')[1] == undefined) {
        es('u-txt j-flag')[0].value = name
    } else {
        es('u-txt j-flag')[1].value = name
    }
    es('u-btn2 u-btn2-2 u-btn2-w2 j-flag')[0].click()
}

var createLists = function (num) {
    for (var i = 1; i <= num; i++) {
        var name = String(i)
        createList(name)
        sleep(5000)
    }
}

var _main = function () {
    var n = numOfSongs()
    var numOfLists = Math.ceil(n / config.num)

    createLists(numOfLists)
    // splitList(n)
}

_main()
