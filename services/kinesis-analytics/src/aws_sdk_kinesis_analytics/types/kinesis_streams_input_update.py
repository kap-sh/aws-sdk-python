"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#KinesisStreamsInputUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.resource_arn
    import aws_sdk_kinesis_analytics.types.role_arn


class KinesisStreamsInputUpdate(TypedDict):
    resource_arn_update: NotRequired[
        "aws_sdk_kinesis_analytics.types.resource_arn.ResourceARN"
    ]
    """<p>Amazon Resource Name (ARN) of the input Amazon Kinesis stream to read.</p>"""
    role_arn_update: NotRequired["aws_sdk_kinesis_analytics.types.role_arn.RoleARN"]
    """<p>ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisStreamsInputUpdate) -> dict:
    out: dict = {}
    if "resource_arn_update" in value:
        out["ResourceARNUpdate"] = value["resource_arn_update"]
    if "role_arn_update" in value:
        out["RoleARNUpdate"] = value["role_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisStreamsInputUpdate:
    out: KinesisStreamsInputUpdate = {}  # type: ignore[typeddict-item]
    if "ResourceARNUpdate" in data:
        out["resource_arn_update"] = data["ResourceARNUpdate"]
    if "RoleARNUpdate" in data:
        out["role_arn_update"] = data["RoleARNUpdate"]
    return out
