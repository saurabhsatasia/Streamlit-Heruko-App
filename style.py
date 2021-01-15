html_temp_1 = """<div style="background-color:rgb(84, 84, 90);padding:5px;border-radius: 10px;box-shadow: 0 0 16px #000, 0 0 32px #000;opacity: 0.7; ">
<h1 style="color:rgba(108, 249, 6, 0.9);text-align:center;">{}</h1>  
</div>"""
# rgb(108, 249, 6) green
# rgba(233, 233, 233, 0.9) gray
html_temp_2 = """<div style="background-color:rgb(84, 84, 90);padding:4px;border-radius: 10px;box-shadow: 0 0 8px #000, 0 0 32px #000;opacity: 0.7;">
        <h4 style="color:rgba(108, 249, 6, 0.9);text-align:center;">{}</h4>
        </div>"""
html_temp_3 = """<div style="background-color:rgb(84, 84, 90);padding:4px;border-radius: 10px;box-shadow: 0 0 8px #000, 0 0 32px #000;opacity: 0.7;">
            <h3 style="color:#EFF5F5;text-align:center;">{} </h3>
            </div>"""



html_style = """<style>
                    .overlay h1 {background-color: #000000;
                                  color: #fff;
                                  mix-blend-mode: multiply;
                                  padding: 6px;
                                  border-radius: 8px;
                                  font-family: arial;
                                  font-size: 3em;
                                  opacity: 0.9;
                                  box-shadow: 0 0 16px #000, 0 0 32px #000;}
                </style>
                <div class="overlay">
                    <h1>{}</h1>
                </div>"""