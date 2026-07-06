"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#KinesisStreamsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.resource_arn


class KinesisStreamsInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The ARN of the input Kinesis data stream to read.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisStreamsInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisStreamsInput:
    out: KinesisStreamsInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("KinesisStreamsInput.resource_arn required")
    return out
