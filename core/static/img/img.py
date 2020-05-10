<body>

    <h1>Index</h1>
    <img src="{% static 'C:\Users\ieda\Desktop\imagemsitee.jpg' %}"/>
    {% for produto in produtos%}
    <p> {{produto.name}} </p>