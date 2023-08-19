function login(){
    let db={0:["logu","agalya@123"],1:["agalya","logu@123"],2:["arrave","logu@123"],3:["krish","logu@123"]};
    let user_name=document.getElementById("user_name").value;
    let password=document.getElementById("password").value;
    let flag=true;
    for(let i=0;i<Object.db[i].length;i++){
        if(user_name==db[i][0]){
            if(password==db[i][1]){
                flag=true;
                break;
            }
        }else{
            flag=false;
        }
    }if(flag==true){
        window.location.href="./home page.HTML";
    }else{
        document.getElementById("result").innerHTML="invalied login"
    }

}