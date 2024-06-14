function validacion() {
 
    // Obtener los valores de los campos de entrada
    var nombre = document.getElementById("nombre").value;
    var correo = document.getElementById("correo").value;
    var seleccion = document.getElementById("rol").selectedIndex;
    var password = document.getElementById("password").value;
    var confirmpassword = document.getElementById("confirmPassword").value;
    var terminos = document.getElementById("terminos").checked;

    // Inicializar una variable de estado para controlar si hay errores
    var hayError = false;

    // Limpiar mensajes de error anteriores
    document.getElementById("mensaje-nombre").innerHTML = "";
    document.getElementById("mensaje-contraseña").innerHTML = "";
    document.getElementById("mensaje-confirmContraseña").innerHTML = "";
    document.getElementById("mensaje-correo").innerHTML = "";
    document.getElementById("mensaje-seleccion").innerHTML = "";
    document.getElementById("mensaje-terminos").innerHTML = "";

    // Validar el nombre
    if (nombre == null || nombre.length == 0) {
        document.getElementById("mensaje-nombre").innerHTML = "⚠️ Debe escribir un nombre";
        hayError = true;
    }
  
    // Validar el correo
    if (correo == null || correo.length == 0) {
        document.getElementById("mensaje-correo").innerHTML = "⚠️ Debe escribir un correo";
        hayError = true;
    } else if (!/^[0-9a-zA-Z._.-]+@[0-9a-zA-Z._.-]+\.[a-zA-Z]{2,6}$/.test(correo)) {
        document.getElementById("mensaje-correo").innerHTML = "⚠️ Debe escribir un correo válido";
        hayError = true;
    }

      // Validar el Rol
      if (seleccion == null || seleccion.length == 0 || seleccion == "") {
        document.getElementById("mensaje-seleccion").innerHTML = "⚠️ Debes seleccionar un rol";
        hayError = true;
    }

     //Validar la contraseña
     if (password == null || password.length == 0) {
        document.getElementById("mensaje-contraseña").innerHTML = "⚠️ Debe escribir una contraseña";
        hayError = true;

    }
    //Validar la confirmación de la contraseña
    if (confirmpassword == null || confirmpassword.length == 0) {
        document.getElementById("mensaje-confirmContraseña").innerHTML = "⚠️ Debe confirmar la contraseña";
        hayError = true;
    } else if (password != confirmpassword) {
        document.getElementById("mensaje-confirmContraseña").innerHTML = "⚠️ Las contraseñas no coinciden";
        document.getElementById("mensaje-contraseña").innerHTML = "⚠️ Las contraseñas no coinciden";
        hayError = true;
    }

    // Validar los términos
    if (!terminos) {
        document.getElementById("mensaje-terminos").innerHTML = "⚠️ Debes aceptar los términos y condiciones";
        hayError = true;
    }
    // Devolver false si hay algún error para evitar el envío del formulario

    return !hayError;
}

