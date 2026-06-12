"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#KinesisFirehoseOutputUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.resource_arn


class KinesisFirehoseOutputUpdate(TypedDict):
    resource_arn_update: "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the delivery stream to write to. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisFirehoseOutputUpdate) -> dict:
    out: dict = {}
    out["ResourceARNUpdate"] = value["resource_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisFirehoseOutputUpdate:
    out: KinesisFirehoseOutputUpdate = {}  # type: ignore[typeddict-item]
    if "ResourceARNUpdate" in data:
        out["resource_arn_update"] = data["ResourceARNUpdate"]
    else:
        raise DeserializationError(
            "KinesisFirehoseOutputUpdate.resource_arn_update required"
        )
    return out
