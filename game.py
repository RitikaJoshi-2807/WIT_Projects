let [computer_score,user_score]=[0,0];
let result_ref=document.getElementById("result");
let choices_object={
  'rock':{
    'rock':'draw',
    'scissor':'win',
    'paper':'lose'
  },
  'paper':{
    'rock':'win',
    'scissor':'lose',
    'paper':'draw'
  },
'scissor':{
    'rock':'lose',
    'scissor':'draw',
    'paper':'win'
  }
}

function checker(input){
  var choice=["rock","paper","scissor"];
  var num=Math.floor(Math.random()*3);
  document.getElementById("comp_choice").innerHTML=
    `Computer choose : <span> ${choice[num].toUpperCase()}</span>`;
  
 
  document.getElementById("user_choice").innerHTML=
    `You choose :<span> ${input.toUpperCase()}</span>`;
  

  let computer_choice=choice[num];
  switch(choices_object[input][computer_choice]){
    case 'lose':
      result_ref.style.cssText="background-color:red; color:white";
      result_ref.innerHTML="YOU LOSE..🥴 BETTER LUCK NEXT TIME";
      computer_score++;
      break;
    case 'win':
      result_ref.style.cssText="background-color:green; color:white";
      result_ref.innerHTML="CONGRATULATIONS..!! 🤩 YOU WIN";
      user_score++;
      break;
    case 'draw':
      result_ref.style.cssText="background-color:yellow; color:black";
      result_ref.innerHTML='DRAW, WELL PLAYED 👍';
      break;
  }
  document.getElementById("computer_score").innerHTML=computer_score;
 document.getElementById("iser_score").innerHTML=user_score;
}
 
