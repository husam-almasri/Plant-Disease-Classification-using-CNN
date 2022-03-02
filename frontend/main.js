var model='Potato';
//Preview & Update an image before it is uploaded
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#img').attr('src', e.target.result);
        }
        image=reader.readAsDataURL(input.files[0]);
    }
    return image
}

$("#imgInp").change(function () {
    readURL(this);
});

$('document').ready(
    function(){
        $('input:radio').click(
            function(){
                $( "#plantId" ).html(event.target.value)
                switch (event.target.value) {
                    case "Potato":
                        model='Potato';
                        document.body.setAttribute("style",
                             "background-image: url('potato_img.jpg');background-repeat: no-repeat;background-color: rgba(255, 255, 255,.8);background-size: 100%;background-blend-mode: soft-light;"
                        );
                        break;
                    case "Tomato":
                        model='Tomato';
                        document.body.setAttribute("style",
                             "background-image: url('tomato_img.jpg');background-repeat: no-repeat;background-color: rgba(255, 255, 255,.8);background-size: 100%;background-blend-mode: soft-light;"
                        );
                        break;
                    case "Pepper":
                        model='Pepper';
                        document.body.setAttribute("style",
                             "background-image: url('pepper_img.jpg');background-repeat: no-repeat;background-color: rgba(255, 255, 255,.8);background-size: 100%;background-blend-mode: soft-light;"
                        );
                        break;
                    default:
                        model='Potato';
                }
               
            }
        );  
    }
);
    
function showResults(data){
    var dataClass = data.class;
    var dataConf = data.confidence;
    if(dataClass=='Healthy'){
        document.getElementById("results").innerHTML ='The plant is: healthy.<br>Confidence level:\t'+dataConf+'%'
    }else{
        document.getElementById("results").innerHTML ='The plant has:\t'+dataClass+'.<br>Confidence level:\t'+dataConf+'%'
    }
}

function makeRequest(){
    var formData = new FormData();
    formData.append('file', $('input[type=file]')[0].files[0]);
    formData.append('plant', model);
    return $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: 'http://localhost:8000/predict',
        data: formData,
        contentType: false,
        processData: false
    });
}
        
if ($('input[type=file]')[0].files.length <= 0) {
    $(document).ready(function() {
        $('#btn').on('click', function() {
            $.when(makeRequest()).then(function successHandler(data){
            //    prediction.innerHTML = data.class;
                showResults(data);
                } ,
                function errorHandler(){
                    console.log('error');
                }
        ); 
        return false;
        });
    });
} 
