"""Generated from Smithy shape ``com.amazonaws.iotevents#AlarmAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.dynamo_d_bv2_action
    import aws_sdk_iot_events.types.dynamo_db_action
    import aws_sdk_iot_events.types.firehose_action
    import aws_sdk_iot_events.types.iot_events_action
    import aws_sdk_iot_events.types.iot_site_wise_action
    import aws_sdk_iot_events.types.iot_topic_publish_action
    import aws_sdk_iot_events.types.lambda_action
    import aws_sdk_iot_events.types.sns_topic_publish_action
    import aws_sdk_iot_events.types.sqs_action

AlarmAction = TypedDict(
    "AlarmAction",
    {
        "sns": NotRequired[
            "aws_sdk_iot_events.types.sns_topic_publish_action.SNSTopicPublishAction"
        ],
        "iot_topic_publish": NotRequired[
            "aws_sdk_iot_events.types.iot_topic_publish_action.IotTopicPublishAction"
        ],
        "lambda": NotRequired["aws_sdk_iot_events.types.lambda_action.LambdaAction"],
        "iot_events": NotRequired[
            "aws_sdk_iot_events.types.iot_events_action.IotEventsAction"
        ],
        "sqs": NotRequired["aws_sdk_iot_events.types.sqs_action.SqsAction"],
        "firehose": NotRequired[
            "aws_sdk_iot_events.types.firehose_action.FirehoseAction"
        ],
        "dynamo_db": NotRequired[
            "aws_sdk_iot_events.types.dynamo_db_action.DynamoDBAction"
        ],
        "dynamo_d_bv2": NotRequired[
            "aws_sdk_iot_events.types.dynamo_d_bv2_action.DynamoDBv2Action"
        ],
        "iot_site_wise": NotRequired[
            "aws_sdk_iot_events.types.iot_site_wise_action.IotSiteWiseAction"
        ],
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: AlarmAction) -> dict:
    out: dict = {}
    if "sns" in value:
        import aws_sdk_iot_events.types.sns_topic_publish_action

        out["sns"] = aws_sdk_iot_events.types.sns_topic_publish_action.serialize_json(
            value["sns"]
        )
    if "iot_topic_publish" in value:
        import aws_sdk_iot_events.types.iot_topic_publish_action

        out["iotTopicPublish"] = (
            aws_sdk_iot_events.types.iot_topic_publish_action.serialize_json(
                value["iot_topic_publish"]
            )
        )
    if "lambda" in value:
        import aws_sdk_iot_events.types.lambda_action

        out["lambda"] = aws_sdk_iot_events.types.lambda_action.serialize_json(
            value["lambda"]
        )
    if "iot_events" in value:
        import aws_sdk_iot_events.types.iot_events_action

        out["iotEvents"] = aws_sdk_iot_events.types.iot_events_action.serialize_json(
            value["iot_events"]
        )
    if "sqs" in value:
        import aws_sdk_iot_events.types.sqs_action

        out["sqs"] = aws_sdk_iot_events.types.sqs_action.serialize_json(value["sqs"])
    if "firehose" in value:
        import aws_sdk_iot_events.types.firehose_action

        out["firehose"] = aws_sdk_iot_events.types.firehose_action.serialize_json(
            value["firehose"]
        )
    if "dynamo_db" in value:
        import aws_sdk_iot_events.types.dynamo_db_action

        out["dynamoDB"] = aws_sdk_iot_events.types.dynamo_db_action.serialize_json(
            value["dynamo_db"]
        )
    if "dynamo_d_bv2" in value:
        import aws_sdk_iot_events.types.dynamo_d_bv2_action

        out["dynamoDBv2"] = aws_sdk_iot_events.types.dynamo_d_bv2_action.serialize_json(
            value["dynamo_d_bv2"]
        )
    if "iot_site_wise" in value:
        import aws_sdk_iot_events.types.iot_site_wise_action

        out["iotSiteWise"] = (
            aws_sdk_iot_events.types.iot_site_wise_action.serialize_json(
                value["iot_site_wise"]
            )
        )
    return out


def deserialize_json(data: dict) -> AlarmAction:
    out: AlarmAction = {}  # type: ignore[typeddict-item]
    if "sns" in data:
        import aws_sdk_iot_events.types.sns_topic_publish_action

        out["sns"] = aws_sdk_iot_events.types.sns_topic_publish_action.deserialize_json(
            data["sns"]
        )
    if "iotTopicPublish" in data:
        import aws_sdk_iot_events.types.iot_topic_publish_action

        out["iot_topic_publish"] = (
            aws_sdk_iot_events.types.iot_topic_publish_action.deserialize_json(
                data["iotTopicPublish"]
            )
        )
    if "lambda" in data:
        import aws_sdk_iot_events.types.lambda_action

        out["lambda"] = aws_sdk_iot_events.types.lambda_action.deserialize_json(
            data["lambda"]
        )
    if "iotEvents" in data:
        import aws_sdk_iot_events.types.iot_events_action

        out["iot_events"] = aws_sdk_iot_events.types.iot_events_action.deserialize_json(
            data["iotEvents"]
        )
    if "sqs" in data:
        import aws_sdk_iot_events.types.sqs_action

        out["sqs"] = aws_sdk_iot_events.types.sqs_action.deserialize_json(data["sqs"])
    if "firehose" in data:
        import aws_sdk_iot_events.types.firehose_action

        out["firehose"] = aws_sdk_iot_events.types.firehose_action.deserialize_json(
            data["firehose"]
        )
    if "dynamoDB" in data:
        import aws_sdk_iot_events.types.dynamo_db_action

        out["dynamo_db"] = aws_sdk_iot_events.types.dynamo_db_action.deserialize_json(
            data["dynamoDB"]
        )
    if "dynamoDBv2" in data:
        import aws_sdk_iot_events.types.dynamo_d_bv2_action

        out["dynamo_d_bv2"] = (
            aws_sdk_iot_events.types.dynamo_d_bv2_action.deserialize_json(
                data["dynamoDBv2"]
            )
        )
    if "iotSiteWise" in data:
        import aws_sdk_iot_events.types.iot_site_wise_action

        out["iot_site_wise"] = (
            aws_sdk_iot_events.types.iot_site_wise_action.deserialize_json(
                data["iotSiteWise"]
            )
        )
    return out
