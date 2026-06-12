"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#KinesisFirehoseDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.string


class KinesisFirehoseDestination(TypedDict):
    delivery_stream_arn: NotRequired["aws_sdk_pinpoint_sms_voice.types.string.String"]
    """The Amazon Resource Name (ARN) of an IAM role that can write data to an Amazon Kinesis Data Firehose stream."""
    iam_role_arn: NotRequired["aws_sdk_pinpoint_sms_voice.types.string.String"]
    """The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose destination that you want to use in the event destination."""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisFirehoseDestination) -> dict:
    out: dict = {}
    if "delivery_stream_arn" in value:
        out["DeliveryStreamArn"] = value["delivery_stream_arn"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    return out


def deserialize_json(data: dict) -> KinesisFirehoseDestination:
    out: KinesisFirehoseDestination = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamArn" in data:
        out["delivery_stream_arn"] = data["DeliveryStreamArn"]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    return out
