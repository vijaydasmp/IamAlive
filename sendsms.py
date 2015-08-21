from twilio.rest import TwilioRestClient
accountSid = "AC4c1b7e0e727f0f294fa663d7aab3a04b"
authToken = "9a0efbfd014ab4d1300265b7bcc82d20"
twilioClient = TwilioRestClient(accountSid, authToken)
myTwilioNumber = "+14012881157"
destCellPhone = "+919860501299"
myMessage = twilioClient.messages.create(body = "Hello  , I am sending you message via twilio", from_=myTwilioNumber, to=destCellPhone)
