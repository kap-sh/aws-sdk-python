"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#KinesisStreamsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.resource_arn
    import aws_sdk_kinesis_analytics.types.role_arn


class KinesisStreamsOutput(TypedDict, closed=True):
    resource_arn: "aws_sdk_kinesis_analytics.types.resource_arn.ResourceARN"
    """<p>ARN of the destination Amazon Kinesis stream to write to.</p>"""
    role_arn: "aws_sdk_kinesis_analytics.types.role_arn.RoleARN"
    """<p>ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisStreamsOutput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisStreamsOutput:
    out: KinesisStreamsOutput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("KinesisStreamsOutput.resource_arn required")
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("KinesisStreamsOutput.role_arn required")
    return out
