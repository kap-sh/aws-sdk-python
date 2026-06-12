"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#KinesisStreamsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.resource_arn


class KinesisStreamsOutput(TypedDict):
    resource_arn: "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The ARN of the destination Kinesis data stream to write to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisStreamsOutput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisStreamsOutput:
    out: KinesisStreamsOutput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("KinesisStreamsOutput.resource_arn required")
    return out
