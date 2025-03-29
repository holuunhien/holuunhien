// ==UserScript==
// @name         SASUKE
// @namespace    http://tampermonkey.net/
// @version      0.5
// @description  Fastest Mass Ejector & Split Macro
// @author       Tom Burris
// @match        https://tranhdau.net/
// @grant        none
// @run-at       document-end
// ==/UserScript==
(function() {
    var local = {
        SCRIPT_CONFIG: {
            NAME_COLOR: "cyan", // the color, which the target name should be changed to
        },
        MENU_CONFIG: {

            /* https://htmlcolorcodes.com/color-picker/ */

            COLOR_1: "#20687C", // you can use color codes, rgba, hsl, rgb or just color names.
            COLOR_2:"#484430", // you can use color codes, rgba, hsl, rgb or just color names.
            RAINBOW: false, // replace false with true if you want the menu to be rainbow.
        },

        // DO NOT CHANGE ANYTHING BELOW HERE UNLESS YOU KNOW WHAT YOU'RE DOING \\

        COLOR_HUE: 0,
        COLOR_HUE2: 300,
        GAME_WS: null,
        GAME_INIT: false,
        PLAYER_PACKET_SPAWN: [],
        PLAYER_SOCKET: null,
        PLAYER_IS_DEAD: false,
        PLAYER_MOUSE: {
            x: null,
            y: null,
        },
        GAME_BYPASS: {
            mouseFrozen: Symbol(),
            utf8: new TextEncoder()
        }
    }

    function changeHue() {
        355 == local.COLOR_HUE && (local.COLOR_HUE = 0), local.COLOR_HUE++;
        355 == local.COLOR_HUE2 && (local.COLOR_HUE2 = 0), local.COLOR_HUE2++;
        $('.dialog-left').css({
            background: 'linear-gradient(to right bottom,hsl('+local.COLOR_HUE+', 50%, 50%),hsl('+local.COLOR_HUE2+', 50%, 50%)'
        })
    }
    function ready() {
        setInterval(() => {
            if(local.MENU_CONFIG.RAINBOW) {
                changeHue()
            } else {
                $('dialog-left').css({
                    background: `linear-gradient(to right bottom,${local.MENU_CONFIG.COLOR_1},${local.MENU_CONFIG.COLOR_2})`
                })
            }
        }, 10)
    }
    const { fillText } = CanvasRenderingContext2D.prototype;
    CanvasRenderingContext2D.prototype.fillText = function(text, x, y) {
        let config = local.SCRIPT_CONFIG
        if(text == document.getElementById("nick").value) {
            this.fillStyle = config.NAME_COLOR;
        }
        fillText.call(this, ...arguments);
    }
    document.addEventListener("DOMContentLoaded", ready)
})();
(function(){
    $("body").dblclick(function(){
        if($("#doubleclick_d").is(":checked"))
            keyPress(68);
    });
    $("head").append("<style>.emberstyle a, #nick, #ip_newserver{border-radius:5px;} #fb_id:hover{text-decoration:none;}</style>");
    newIns();
    var interval_gold, interval_bomb, key = false, key2 = false, att=20, X=0, Y=0, k=0, fg=false;

    function autoSpawn()
    {
        setInterval(function(){
            if($("#overlays").is(':visible') && $("#autorespawnok").is(":checked"))
                $('.btn-play-guest')[0].click();
        },1000)
    }

    function newIns(){
              var skinInput = document.getElementById("skin");
        if (skinInput) {
            skinInput.value = "202503230113110386491001742731991"; // thay id skin o day !
        }

    }
    $(document).on('keydown',function(e){
        // Doublesplit -> key2
        if (e.keyCode == 50)
        {
        }

        else if(e.keyCode == 80 && !$("#nick, #ip_newserver, #chat_textbox").is(":focus"))
        {
            $('.btn-play-guest')[0].click();
            $("#overlays").css("display","none");
        }


        else if(e.keyCode == 82)

        {
        }
        //=============================== mo =====================================
        else if(e.keyCode == 90  && e.ctrlKey){
			$('#close_chatfull').click(function(){$(this).fadeOut("fast");});
            setSkins(true); //Skins: false
            $('#screenshot, #account_button, .controls, #klan, #level, #stats, .tosBox').remove();
            $("#gamemode").replaceWith(
                ' </div></div>');
            $("#bilgilerModal").html('<div class="modal-dialog modal-sm"><div class="modal-content"><div class="modal-header">Emoji<button type="button" class="close" data-dismiss="modal">&times;</button></div><div class="modal-body"><h3>'+
                                     '<button></button>&nbsp;<button></button>&nbsp;<button></button>&nbsp;<button></button>&nbsp;<button></button>&nbsp;</h3></div></div></div>');

            $("#chat_textbox").attr("maxlength","70");
            $("#loginModal div.modal-content").replaceWith('<div class="modal-header">'+
                                                           '<button type="button" id="close_chatfull" class="close" data-dismiss="modal">&times;</button><h1 style="text-align:center;color:#FF0000;" class="modal-title">Hmmm..<br> Chat is full!</h1></div>');
        }
        //=============================== tat =====================================
        else if(e.keyCode == 88  && e.ctrlKey){
			$('#close_chatfull').click(function(){$(this).fadeOut("fast");});
            setSkins(false); //Skins: false
            $('#screenshot, #account_button, .controls, #klan, #level, #stats, .tosBox').remove();
            $("#gamemode").replaceWith(
                ' </div></div>');
            $("#bilgilerModal").html('<div class="modal-dialog modal-sm"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal">&times;</button></div><div class="modal-body"><h3>'+
                                     '<button></button>&nbsp;<button></button>&nbsp;<button></button>&nbsp;<button></button>&nbsp;<button></button>&nbsp;</h3></div></div></div>');
            $("#chat_textbox").attr("maxlength","70");
            $("#loginModal div.modal-content").replaceWith('<div class="modal-header">'+
                                                           '<button type="button" id="close_chatfull" class="close" data-dismiss="modal">&times;</button><h1 style="text-align:center;color:#FF0000;" class="modal-title">Hmmm..<br> Chat is full!</h1></div>');


        }
            //=============================== moAcid =====================================
        else if(e.keyCode == 67  && e.ctrlKey){
			$('#close_chatfull').click(function(){$(this).fadeOut("fast");});
            setNames(true);//Acid:true
            $('#screenshot, #account_button, .controls, #klan, #level, #stats, .tosBox').remove();
            $("#gamemode").replaceWith(
                ' </div></div>');
            $("#bilgilerModal").html('<div class="modal-dialog modal-sm"><div class="modal-content"><div class="modal-header">Emoji<button type="button" class="close" data-dismiss="modal">&times;</button></div><div class="modal-body"><h3>'+
                                     '<button></button>&nbsp;<button></button>&nbsp;<button></button>&nbsp;<button></button>&nbsp;<button></button>&nbsp;</h3></div></div></div>');

            $("#chat_textbox").attr("maxlength","70");
            $("#loginModal div.modal-content").replaceWith('<div class="modal-header">'+
                                                           '<button type="button" id="close_chatfull" class="close" data-dismiss="modal">&times;</button><h1 style="text-align:center;color:#FF0000;" class="modal-title">Hmmm..<br> Chat is full!</h1></div>');
        }
                    //=============================== TatAcide =====================================
else if(e.keyCode == 86  && e.ctrlKey){
			$('#close_chatfull').click(function(){$(this).fadeOut("fast");});
             setNames(false);//Acid: false
            $('#screenshot, #account_button, .controls, #klan, #level, #stats, .tosBox').remove();
            $("#gamemode").replaceWith(
                ' </div></div>');
            $("#bilgilerModal").html('<div class="modal-dialog modal-sm"><div class="modal-content"><div class="modal-header">Emoji<button type="button" class="close" data-dismiss="modal">&times;</button></div><div class="modal-body"><h3>'+
                                     '<button></button>&nbsp;<button></button>&nbsp;<button></button>&nbsp;<button></button>&nbsp;<button></button>&nbsp;</h3></div></div></div>');

            $("#chat_textbox").attr("maxlength","70");
            $("#loginModal div.modal-content").replaceWith('<div class="modal-header">'+
                                                           '<button type="button" id="close_chatfull" class="close" data-dismiss="modal">&times;</button><h1 style="text-align:center;color:#FF0000;" class="modal-title">Hmmm..<br> Chat is full!</h1></div>');
        }
// ...

// ...
                    //=============================== tat =====================================

    })
                })
();


var script = document.createElement('script');
(document.body || document.head || document.documentElement).appendChild(script);
        $("#instructions").hide();
        $("#adbg").hide();
        $("#footer").hide();
        $("#instructions").hide();
        $("#settings-btn").remove();
        $("#canvasx").hide();
        $('.dialog-right').hide();
        $('.btn-danger').hide();
        $('.progress-bar-text').hide();
        $('.agario-exp-bar').hide();
        $('.progress-bar-star').hide();
        $("#gamemode").remove();



        $('.agario-profile-picture').replaceWith ('<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmJvaXhzNXdtdXpwNzdhNnQ5YmpmbXFsZW5uaTV1bzJocG8xYXdvbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FB5EOw0CaaQM0/giphy.gif" style=\" right: 70%; width: 100%; height: 210px;;\ ">')
        $("#overlays").append('<img src="https://i.imgur.com/Kio4vMr.gif" style="width:100%; height:1080px; display:inline-block;">');
        $(".dialog-left").append ('<marquee   width="100%" height="100%" style=""><font color=Blue>WELCOM TO PRESENTATION Luu Nhien</marquee>')
        $('.dialog-left').css({color: 'rgba(255, 255, 255, 1)', 'background-color': 'rgba(0, 0, 0, 0.5)'})
        $('.agario-panel').css({color: 'rgba(255, 255, 255, 1)', 'background-color': 'rgba(0, 0, 0, 0.5)'})
        $('.btn-primary').css({color: 'rgba(255, 255, 255, 1)', 'background-color': 'rgba(0, 0, 0, 0.5)'})
        $('.btn-needs-server').css({color: 'rgba(255, 255, 255, 1)', 'background-color': 'rgba(0, 0, 0, 0.5)'})
        $('.btn-primary').text('Skin');
        $(".btn-play").text('Play');


window.addEventListener('keydown', keydown);
window.addEventListener('keyup', keyup);
var Feed = false;
var Speed = 50;

//Funtions
function split() {
    $("body").trigger($.Event("keydown", { keyCode: 32}));
    $("body").trigger($.Event("keyup", { keyCode: 32}));
}
function mass() {
    if (Feed) {
        window.onkeydown({keyCode: 87});
        window.onkeyup({keyCode: 87});
        setTimeout(mass, Speed);
    }
}

function keydown(event) {
    switch(event.keyCode){
    // Feed Macro
    case 81:                                        // Q
    {
        Feed = true;
        setTimeout(mass,Speed);
    }// Center
    case 83:                                       // S
        X = window.innerWidth/2;
        Y = window.innerHeight/2;
        $("canvas").trigger($.Event("mousemove", {clientX: X,clientY: Y}));

    break; // Triplesplit
    case 68:         //  and Put in Your Key
        split();
        setTimeout(split, Speed);
        setTimeout(split, Speed*2);
    break; // Doublesplit
    case 65:         // A and Put in Your Key
        split();
        setTimeout(split, Speed);
    break;

    }
} // When Player Lets Go Of Q,It Stops Feeding
function keyup(event) {
    if (event.keyCode == 81) {
        Feed = false;
    }
}

//Mouse Clicks
(function() {
    $("#canvas").bind("mousedown",function(event) {
        switch(event.which){
        case 1:

        break;
        case 2:

        break;
        case 3:
            Feed = true;
            setTimeout(mass, Speed);
        break;
        }
    });

    $("#canvas").bind("mouseup",function(event) {
        if (event.which == 3) {
            Feed = false;
        }
    });
    $('#canvas').bind('contextmenu',function(e) {
        e.preventDefault();
    });
}());



(function() {
'use strict';

var New_WhiteBackgroundColor = '#000';

var old_fillRect = CanvasRenderingContext2D.prototype.fillRect;
CanvasRenderingContext2D.prototype.fillRect = function() {
    var x = arguments[0];
    var y = arguments[1];
    var w = arguments[2];
    var h = arguments[3];

    if (x==0 && y==0 && w==this.canvas.width && h==this.canvas.height) {
        if (this.fillStyle == '#f2fbff') {
            this.fillStyle = New_WhiteBackgroundColor;
        }
    }

    return old_fillRect.apply(this, arguments);
};

function calculateRemain(text) {
    if (text.endsWith('s')) {
        var match;

        match = / in:? (\d+)s$/.exec(text);
        if (match !== null) {
            return parseInt(match[1], 10);
        }

        match = /^((\d+)m)? ?(\d+)s$/.exec(text);
        if (match !== null) {
            return (parseInt(match[2], 10) || 0) * 60 + parseInt(match[3], 10); // "x || 0" is "0 if x undefined"
        }
    }

    return null;
}

var old_fillText = CanvasRenderingContext2D.prototype.fillText;
CanvasRenderingContext2D.prototype.fillText = function() {
    if (arguments[0]=='Leaderboard')
        arguments[0] = '   PRCTOWN'
    return old_fillText.apply(this, arguments);
};
})();
var z = "";
var x = "";;
var i = document.getElementById("helloDialog");
var t ="";;;










class mouseWheelZoom {
  constructor() {
    this.mOX = 0;
    this.mOY = 0;
    this.zoomValue = 0;
    this.cellX = 0;
    this.cellY = 0;


  }
  createBuffer(length) {
    return new DataView(new ArrayBuffer(length));
  }
  sendBuffer(buf) {
    if(this.ws && this.ws.readyState == 1) this.ws.send(buf);
  }




  sendMousePacket() {
    let buffer = this.createBuffer(29);
    buffer.setUint8(0, 4);
    buffer.setFloat64(1, ((window.clientXXX - window.innerWidth / 2) / this.zoomValue) + this.cellX, true);
    buffer.setFloat64(9, ((window.clientYYY - window.innerHeight / 2) / this.zoomValue) + this.cellY, true);
    buffer.setFloat64(17, 0, true);
    buffer.setUint32(25, true);
    this.sendBuffer(buffer);
  }

}

var observer = new MutationObserver(function(mutations){
  mutations.forEach(function(mutation) {
    mutation.addedNodes.forEach(function(node) {
      if (/agario\.core\.js/i.test(node.src)){
        observer.disconnect();
        node.parentNode.removeChild(node);
        var request = new XMLHttpRequest();
        request.open("get", node.src, true);
        request.send();
        request.onload = function(){
          var coretext = this.responseText;
          var newscript = document.createElement("script");
          newscript.type = "text/javascript";
          newscript.async = true;
          window._op = new mouseWheelZoom();
          newscript.textContent = replaceCore(coretext);
          document.body.appendChild(newscript);
        };
      }
    });
  });
});
observer.observe(document, {attributes:true, characterData:true, childList:true, subtree:true});

const replaceCore = core => {
  core = core.replace(/;if\((\w)<1\.0\){/i, `;if(0){`);
  core = core.replace(/0;\w\[\w\+...>>3\]=(\w);\w\[\w\+...>>3\]=(\w);\w\[\w\+...>>3\]=(\w);\w\[\w\+...>>3\]=(\w);/i, `$& if(Math.abs($3-$1)>14e3 && Math.abs($4-$2)>14e3){window._op.mOX = ($1+$3)/2; window._op.mOY = ($2+$4)/2};`);


  return core;
}
