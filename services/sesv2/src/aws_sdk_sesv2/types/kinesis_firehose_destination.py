"""Generated from Smithy shape ``com.amazonaws.sesv2#KinesisFirehoseDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.amazon_resource_name


class KinesisFirehoseDestination(TypedDict, closed=True):
    iam_role_arn: "aws_sdk_sesv2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the IAM role that the Amazon SES API v2 uses to send email events to the Amazon Kinesis Data Firehose stream.</p>"""
    delivery_stream_arn: "aws_sdk_sesv2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that the Amazon SES API v2 sends email events to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisFirehoseDestination) -> dict:
    out: dict = {}
    out["IamRoleArn"] = value["iam_role_arn"]
    out["DeliveryStreamArn"] = value["delivery_stream_arn"]
    return out


def deserialize_json(data: dict) -> KinesisFirehoseDestination:
    out: KinesisFirehoseDestination = {}  # type: ignore[typeddict-item]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError("KinesisFirehoseDestination.iam_role_arn required")
    if "DeliveryStreamArn" in data:
        out["delivery_stream_arn"] = data["DeliveryStreamArn"]
    else:
        raise DeserializationError(
            "KinesisFirehoseDestination.delivery_stream_arn required"
        )
    return out
