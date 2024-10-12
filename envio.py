import resend

resend.api_key = "mi_clave_de_resend"

r = resend.Emails.send({
  "from": "onboarding@resend.dev",
  "to": "nombre_mail@outlook.com",
  "subject": "Hello World",
  "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})
