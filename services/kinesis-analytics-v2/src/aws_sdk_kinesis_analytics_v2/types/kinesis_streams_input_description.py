"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#KinesisStreamsInputDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.resource_arn
    import aws_sdk_kinesis_analytics_v2.types.role_arn


class KinesisStreamsInputDescription(TypedDict):
    resource_arn: "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the Kinesis data stream.</p>"""
    role_arn: NotRequired["aws_sdk_kinesis_analytics_v2.types.role_arn.RoleARN"]
    """<p>The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.</p> <note> <p>Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisStreamsInputDescription) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisStreamsInputDescription:
    out: KinesisStreamsInputDescription = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError(
            "KinesisStreamsInputDescription.resource_arn required"
        )
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    return out
