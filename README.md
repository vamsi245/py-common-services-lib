# **AWS Lambda logging**

This projects provides a function to log AWS Lambda executions to cloudwatch.   

#### **Requirements**  
- python
#### **Usage**

```python
from common_services import create_log_message

def handle_request(event,context):
    log = create_log_message.CreateAuditMessage(context=context)
    log.createauditmessage(business_key="test",business_value="test",log_level="INFO",trace_id="12334",information="this is a info message",message="received")

```

#### **Structuring AWS Lambda Logs**

1. Use the CreateAuditMessage_class.py to structure your logs as a json
2. Below are the logs structured when used the CreateAuditMessage_Class. 
  
     **Received:**
      ```json
    {
        "timestamp": "2020-03-05T22:40:51",
        "logEvent": "Received",
        "logGroup": "/aws/lambda/ship-gr-idoc-to-fusion-connectivity",
        "logStream": "2020/03/05/[$LATEST]33d7348572e14ec48efa0ea7f9745d9f",
        "logLevel": "INFO",
        "componentName": "ship-gr-idoc-to-fusion-connectivity",
        "traceId": "a158f731-c424-44af-84fb-aca07fb9a0f7",
        "businessKeyStructure": "InboundDelivery|RefId|PlantCode|TrackingId",
        "businessKeyValue": "533197700-533197700|Vamsi-64ee-49f3-abc8-d2c49edc1139|1062|a158f731-c424-44af-84fb-aca07fb9a0f7",
        "businessKey": {
            "InboundDelivery": "533197700-533197700",
            "RefId": "Vamsi-64ee-49f3-abc8-d2c49edc1139",
            "PlantCode": "1062"
         },
        "awsRequestId": "22793623-886c-530e-b173-60f80a49aac1"
    }
    ```
     **Delivered:**
      ```json
    {
            "timestamp": "2020-03-05T22:40:51",
            "logEvent": "Delivered",
            "logGroup": "/aws/lambda/ship-gr-idoc-to-fusion-connectivity",
            "logStream": "2020/03/05/[$LATEST]33d7348572e14ec48efa0ea7f9745d9f",
            "logLevel": "INFO",
            "componentName": "ship-gr-idoc-to-fusion-connectivity",
            "traceId": "a158f731-c424-44af-84fb-aca07fb9a0f7",
            "businessKeyStructure": "InboundDelivery|RefId|PlantCode|TrackingId",
            "businessKeyValue": "533197700-533197700|Vamsi-64ee-49f3-abc8-d2c49edc1139|1062|a158f731-c424-44af-84fb-aca07fb9a0f7",
            "businessKey": {
                "InboundDelivery": "533197700-533197700",
                "RefId": "Vamsi-64ee-49f3-abc8-d2c49edc1139",
                "PlantCode": "1062"
             },
            "awsRequestId": "22793623-886c-530e-b173-60f80a49aac1"
        }
    ```
   
     **Discarded:**
      ```json
    {
            "timestamp": "2020-03-05T22:40:51",
            "logEvent": "Discarded",
            "message" : "Invalid Carton number",
            "logGroup": "/aws/lambda/ship-gr-idoc-to-fusion-connectivity",
            "logStream": "2020/03/05/[$LATEST]33d7348572e14ec48efa0ea7f9745d9f",
            "logLevel": "INFO",
            "componentName": "ship-gr-idoc-to-fusion-connectivity",
            "traceId": "a158f731-c424-44af-84fb-aca07fb9a0f7",
            "businessKeyStructure": "InboundDelivery|RefId|PlantCode|TrackingId",
            "businessKeyValue": "533197700-533197700|Vamsi-64ee-49f3-abc8-d2c49edc1139|1062|a158f731-c424-44af-84fb-aca07fb9a0f7",
            "businessKey": {
                "InboundDelivery": "533197700-533197700",
                "RefId": "Vamsi-64ee-49f3-abc8-d2c49edc1139",
                "PlantCode": "1062"
             },
            "awsRequestId": "22793623-886c-530e-b173-60f80a49aac1"
        }
    ```
   
    **Failure:**
      ```json
    {
        "timestamp": "2020-03-05T22:40:53",
        "message": "An exception of type Exception occurred. Arguments:('Tansient Error while posting to fusion. Message will be retried OSB Service Callout action received SOAP Fault response',)",
        "logEvent": "Failure",
        "logGroup": "/aws/lambda/ship-gr-idoc-to-fusion-connectivity",
        "logStream": "2020/03/05/[$LATEST]33d7348572e14ec48efa0ea7f9745d9f",
        "logLevel": "ERROR",
        "componentName": "ship-gr-idoc-to-fusion-connectivity",
        "traceId": "a158f731-c424-44af-84fb-aca07fb9a0f7",
        "businessKeyStructure": "InboundDelivery|RefId|PlantCode|TrackingId",
        "businessKeyValue": "533197700-533197700|Vamsi-64ee-49f3-abc8-d2c49edc1139|1062|a158f731-c424-44af-84fb-aca07fb9a0f7",
        "businessKey": {
            "InboundDelivery": "533197700-533197700",
            "RefId": "Vamsi-64ee-49f3-abc8-d2c49edc1139",
            "PlantCode": "1062",
            "TrackingId": "a158f731-c424-44af-84fb-aca07fb9a0f7"
        },
        "awsRequestId": "22793623-886c-530e-b173-60f80a49aac1"
    }
    ```

3. It is recommended to write a Received log when the lambda is invoked and Delivered audit when the lambda execution is completed. This helps us to track the transaction status in the lambda. The business keys are unique attributes that can identify an event. Chose the business keys as per your business needs. When need be, we can create reports and stats using these business keys
4. When the logs are structured as outlined above, we can create a Splunk dashboard using the below method

