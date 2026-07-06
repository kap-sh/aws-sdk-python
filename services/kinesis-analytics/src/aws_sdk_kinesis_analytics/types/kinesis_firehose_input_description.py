"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#KinesisFirehoseInputDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.resource_arn
    import aws_sdk_kinesis_analytics.types.role_arn


class KinesisFirehoseInputDescription(TypedDict, closed=True):
    resource_arn: NotRequired[
        "aws_sdk_kinesis_analytics.types.resource_arn.ResourceARN"
    ]
    """<p>Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.</p>"""
    role_arn: NotRequired["aws_sdk_kinesis_analytics.types.role_arn.RoleARN"]
    """<p>ARN of the IAM role that Amazon Kinesis Analytics assumes to access the stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisFirehoseInputDescription) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisFirehoseInputDescription:
    out: KinesisFirehoseInputDescription = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    return out
