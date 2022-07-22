## AWS Demo Server API
This folder contains an example real world AWS API. The API function accepts `region_name` as an input argument and returns the list of EC2 instances in that region, as an output response. In order to make the API pass all the tests done by `schemathesis`, we try to raise various kinds of HTTP Error Exceptions for various _incorrect_ input scenarios.

To run this python script, you would need AWS boto3 session credentials saved in the `aws_credentials.json` file and this json file should be in the same directory as the `aws_demo_server.py` file.

The contents of the `aws_credentials.json` file will be as below:
```
{
"AccessKeyId": "ASIAYOGUWMUMLQLSEABL",
"SecretAccessKey": "abcd12345678qwerty",
"SessionToken": "+ReallyLongRandomToken",
"Expiration": "2022-07-12T06:51:40+00:00"
}
```

I used `boto3.assume_role()` operation to generate the above credentials, but if you have root account CLI credentials which has access to all the AWS services you could pass that directly in this `aws_credentials.json` file.

**Resources** :<br>
Be sure to check the following resources below to raise the correct HTTP Error code for your exception handling of the input arguments.
* https://www.restapitutorial.com/httpstatuscodes.html
* [Wikipedia - List of HTTP Error Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) 