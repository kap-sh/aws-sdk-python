"""Generated from Smithy shape ``com.amazonaws.iot#Action``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.cloudwatch_alarm_action
    import aws_sdk_iot.types.cloudwatch_logs_action
    import aws_sdk_iot.types.cloudwatch_metric_action
    import aws_sdk_iot.types.dynamo_d_bv2_action
    import aws_sdk_iot.types.dynamo_db_action
    import aws_sdk_iot.types.elasticsearch_action
    import aws_sdk_iot.types.firehose_action
    import aws_sdk_iot.types.http_action
    import aws_sdk_iot.types.iot_analytics_action
    import aws_sdk_iot.types.iot_events_action
    import aws_sdk_iot.types.iot_site_wise_action
    import aws_sdk_iot.types.kafka_action
    import aws_sdk_iot.types.kinesis_action
    import aws_sdk_iot.types.lambda_action
    import aws_sdk_iot.types.location_action
    import aws_sdk_iot.types.open_search_action
    import aws_sdk_iot.types.republish_action
    import aws_sdk_iot.types.s3_action
    import aws_sdk_iot.types.salesforce_action
    import aws_sdk_iot.types.sns_action
    import aws_sdk_iot.types.sqs_action
    import aws_sdk_iot.types.step_functions_action
    import aws_sdk_iot.types.timestream_action

Action = TypedDict(
    "Action",
    {
        "dynamo_db": NotRequired["aws_sdk_iot.types.dynamo_db_action.DynamoDBAction"],
        "dynamo_d_bv2": NotRequired[
            "aws_sdk_iot.types.dynamo_d_bv2_action.DynamoDBv2Action"
        ],
        "lambda": NotRequired["aws_sdk_iot.types.lambda_action.LambdaAction"],
        "sns": NotRequired["aws_sdk_iot.types.sns_action.SnsAction"],
        "sqs": NotRequired["aws_sdk_iot.types.sqs_action.SqsAction"],
        "kinesis": NotRequired["aws_sdk_iot.types.kinesis_action.KinesisAction"],
        "republish": NotRequired["aws_sdk_iot.types.republish_action.RepublishAction"],
        "s3": NotRequired["aws_sdk_iot.types.s3_action.S3Action"],
        "firehose": NotRequired["aws_sdk_iot.types.firehose_action.FirehoseAction"],
        "cloudwatch_metric": NotRequired[
            "aws_sdk_iot.types.cloudwatch_metric_action.CloudwatchMetricAction"
        ],
        "cloudwatch_alarm": NotRequired[
            "aws_sdk_iot.types.cloudwatch_alarm_action.CloudwatchAlarmAction"
        ],
        "cloudwatch_logs": NotRequired[
            "aws_sdk_iot.types.cloudwatch_logs_action.CloudwatchLogsAction"
        ],
        "elasticsearch": NotRequired[
            "aws_sdk_iot.types.elasticsearch_action.ElasticsearchAction"
        ],
        "salesforce": NotRequired[
            "aws_sdk_iot.types.salesforce_action.SalesforceAction"
        ],
        "iot_analytics": NotRequired[
            "aws_sdk_iot.types.iot_analytics_action.IotAnalyticsAction"
        ],
        "iot_events": NotRequired[
            "aws_sdk_iot.types.iot_events_action.IotEventsAction"
        ],
        "iot_site_wise": NotRequired[
            "aws_sdk_iot.types.iot_site_wise_action.IotSiteWiseAction"
        ],
        "step_functions": NotRequired[
            "aws_sdk_iot.types.step_functions_action.StepFunctionsAction"
        ],
        "timestream": NotRequired[
            "aws_sdk_iot.types.timestream_action.TimestreamAction"
        ],
        "http": NotRequired["aws_sdk_iot.types.http_action.HttpAction"],
        "kafka": NotRequired["aws_sdk_iot.types.kafka_action.KafkaAction"],
        "open_search": NotRequired[
            "aws_sdk_iot.types.open_search_action.OpenSearchAction"
        ],
        "location": NotRequired["aws_sdk_iot.types.location_action.LocationAction"],
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    out: dict = {}
    if "dynamo_db" in value:
        import aws_sdk_iot.types.dynamo_db_action

        out["dynamoDB"] = aws_sdk_iot.types.dynamo_db_action.serialize_json(
            value["dynamo_db"]
        )
    if "dynamo_d_bv2" in value:
        import aws_sdk_iot.types.dynamo_d_bv2_action

        out["dynamoDBv2"] = aws_sdk_iot.types.dynamo_d_bv2_action.serialize_json(
            value["dynamo_d_bv2"]
        )
    if "lambda" in value:
        import aws_sdk_iot.types.lambda_action

        out["lambda"] = aws_sdk_iot.types.lambda_action.serialize_json(value["lambda"])
    if "sns" in value:
        import aws_sdk_iot.types.sns_action

        out["sns"] = aws_sdk_iot.types.sns_action.serialize_json(value["sns"])
    if "sqs" in value:
        import aws_sdk_iot.types.sqs_action

        out["sqs"] = aws_sdk_iot.types.sqs_action.serialize_json(value["sqs"])
    if "kinesis" in value:
        import aws_sdk_iot.types.kinesis_action

        out["kinesis"] = aws_sdk_iot.types.kinesis_action.serialize_json(
            value["kinesis"]
        )
    if "republish" in value:
        import aws_sdk_iot.types.republish_action

        out["republish"] = aws_sdk_iot.types.republish_action.serialize_json(
            value["republish"]
        )
    if "s3" in value:
        import aws_sdk_iot.types.s3_action

        out["s3"] = aws_sdk_iot.types.s3_action.serialize_json(value["s3"])
    if "firehose" in value:
        import aws_sdk_iot.types.firehose_action

        out["firehose"] = aws_sdk_iot.types.firehose_action.serialize_json(
            value["firehose"]
        )
    if "cloudwatch_metric" in value:
        import aws_sdk_iot.types.cloudwatch_metric_action

        out["cloudwatchMetric"] = (
            aws_sdk_iot.types.cloudwatch_metric_action.serialize_json(
                value["cloudwatch_metric"]
            )
        )
    if "cloudwatch_alarm" in value:
        import aws_sdk_iot.types.cloudwatch_alarm_action

        out["cloudwatchAlarm"] = (
            aws_sdk_iot.types.cloudwatch_alarm_action.serialize_json(
                value["cloudwatch_alarm"]
            )
        )
    if "cloudwatch_logs" in value:
        import aws_sdk_iot.types.cloudwatch_logs_action

        out["cloudwatchLogs"] = aws_sdk_iot.types.cloudwatch_logs_action.serialize_json(
            value["cloudwatch_logs"]
        )
    if "elasticsearch" in value:
        import aws_sdk_iot.types.elasticsearch_action

        out["elasticsearch"] = aws_sdk_iot.types.elasticsearch_action.serialize_json(
            value["elasticsearch"]
        )
    if "salesforce" in value:
        import aws_sdk_iot.types.salesforce_action

        out["salesforce"] = aws_sdk_iot.types.salesforce_action.serialize_json(
            value["salesforce"]
        )
    if "iot_analytics" in value:
        import aws_sdk_iot.types.iot_analytics_action

        out["iotAnalytics"] = aws_sdk_iot.types.iot_analytics_action.serialize_json(
            value["iot_analytics"]
        )
    if "iot_events" in value:
        import aws_sdk_iot.types.iot_events_action

        out["iotEvents"] = aws_sdk_iot.types.iot_events_action.serialize_json(
            value["iot_events"]
        )
    if "iot_site_wise" in value:
        import aws_sdk_iot.types.iot_site_wise_action

        out["iotSiteWise"] = aws_sdk_iot.types.iot_site_wise_action.serialize_json(
            value["iot_site_wise"]
        )
    if "step_functions" in value:
        import aws_sdk_iot.types.step_functions_action

        out["stepFunctions"] = aws_sdk_iot.types.step_functions_action.serialize_json(
            value["step_functions"]
        )
    if "timestream" in value:
        import aws_sdk_iot.types.timestream_action

        out["timestream"] = aws_sdk_iot.types.timestream_action.serialize_json(
            value["timestream"]
        )
    if "http" in value:
        import aws_sdk_iot.types.http_action

        out["http"] = aws_sdk_iot.types.http_action.serialize_json(value["http"])
    if "kafka" in value:
        import aws_sdk_iot.types.kafka_action

        out["kafka"] = aws_sdk_iot.types.kafka_action.serialize_json(value["kafka"])
    if "open_search" in value:
        import aws_sdk_iot.types.open_search_action

        out["openSearch"] = aws_sdk_iot.types.open_search_action.serialize_json(
            value["open_search"]
        )
    if "location" in value:
        import aws_sdk_iot.types.location_action

        out["location"] = aws_sdk_iot.types.location_action.serialize_json(
            value["location"]
        )
    return out


def deserialize_json(data: dict) -> Action:
    out: Action = {}  # type: ignore[typeddict-item]
    if "dynamoDB" in data:
        import aws_sdk_iot.types.dynamo_db_action

        out["dynamo_db"] = aws_sdk_iot.types.dynamo_db_action.deserialize_json(
            data["dynamoDB"]
        )
    if "dynamoDBv2" in data:
        import aws_sdk_iot.types.dynamo_d_bv2_action

        out["dynamo_d_bv2"] = aws_sdk_iot.types.dynamo_d_bv2_action.deserialize_json(
            data["dynamoDBv2"]
        )
    if "lambda" in data:
        import aws_sdk_iot.types.lambda_action

        out["lambda"] = aws_sdk_iot.types.lambda_action.deserialize_json(data["lambda"])
    if "sns" in data:
        import aws_sdk_iot.types.sns_action

        out["sns"] = aws_sdk_iot.types.sns_action.deserialize_json(data["sns"])
    if "sqs" in data:
        import aws_sdk_iot.types.sqs_action

        out["sqs"] = aws_sdk_iot.types.sqs_action.deserialize_json(data["sqs"])
    if "kinesis" in data:
        import aws_sdk_iot.types.kinesis_action

        out["kinesis"] = aws_sdk_iot.types.kinesis_action.deserialize_json(
            data["kinesis"]
        )
    if "republish" in data:
        import aws_sdk_iot.types.republish_action

        out["republish"] = aws_sdk_iot.types.republish_action.deserialize_json(
            data["republish"]
        )
    if "s3" in data:
        import aws_sdk_iot.types.s3_action

        out["s3"] = aws_sdk_iot.types.s3_action.deserialize_json(data["s3"])
    if "firehose" in data:
        import aws_sdk_iot.types.firehose_action

        out["firehose"] = aws_sdk_iot.types.firehose_action.deserialize_json(
            data["firehose"]
        )
    if "cloudwatchMetric" in data:
        import aws_sdk_iot.types.cloudwatch_metric_action

        out["cloudwatch_metric"] = (
            aws_sdk_iot.types.cloudwatch_metric_action.deserialize_json(
                data["cloudwatchMetric"]
            )
        )
    if "cloudwatchAlarm" in data:
        import aws_sdk_iot.types.cloudwatch_alarm_action

        out["cloudwatch_alarm"] = (
            aws_sdk_iot.types.cloudwatch_alarm_action.deserialize_json(
                data["cloudwatchAlarm"]
            )
        )
    if "cloudwatchLogs" in data:
        import aws_sdk_iot.types.cloudwatch_logs_action

        out["cloudwatch_logs"] = (
            aws_sdk_iot.types.cloudwatch_logs_action.deserialize_json(
                data["cloudwatchLogs"]
            )
        )
    if "elasticsearch" in data:
        import aws_sdk_iot.types.elasticsearch_action

        out["elasticsearch"] = aws_sdk_iot.types.elasticsearch_action.deserialize_json(
            data["elasticsearch"]
        )
    if "salesforce" in data:
        import aws_sdk_iot.types.salesforce_action

        out["salesforce"] = aws_sdk_iot.types.salesforce_action.deserialize_json(
            data["salesforce"]
        )
    if "iotAnalytics" in data:
        import aws_sdk_iot.types.iot_analytics_action

        out["iot_analytics"] = aws_sdk_iot.types.iot_analytics_action.deserialize_json(
            data["iotAnalytics"]
        )
    if "iotEvents" in data:
        import aws_sdk_iot.types.iot_events_action

        out["iot_events"] = aws_sdk_iot.types.iot_events_action.deserialize_json(
            data["iotEvents"]
        )
    if "iotSiteWise" in data:
        import aws_sdk_iot.types.iot_site_wise_action

        out["iot_site_wise"] = aws_sdk_iot.types.iot_site_wise_action.deserialize_json(
            data["iotSiteWise"]
        )
    if "stepFunctions" in data:
        import aws_sdk_iot.types.step_functions_action

        out["step_functions"] = (
            aws_sdk_iot.types.step_functions_action.deserialize_json(
                data["stepFunctions"]
            )
        )
    if "timestream" in data:
        import aws_sdk_iot.types.timestream_action

        out["timestream"] = aws_sdk_iot.types.timestream_action.deserialize_json(
            data["timestream"]
        )
    if "http" in data:
        import aws_sdk_iot.types.http_action

        out["http"] = aws_sdk_iot.types.http_action.deserialize_json(data["http"])
    if "kafka" in data:
        import aws_sdk_iot.types.kafka_action

        out["kafka"] = aws_sdk_iot.types.kafka_action.deserialize_json(data["kafka"])
    if "openSearch" in data:
        import aws_sdk_iot.types.open_search_action

        out["open_search"] = aws_sdk_iot.types.open_search_action.deserialize_json(
            data["openSearch"]
        )
    if "location" in data:
        import aws_sdk_iot.types.location_action

        out["location"] = aws_sdk_iot.types.location_action.deserialize_json(
            data["location"]
        )
    return out
