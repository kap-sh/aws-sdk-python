"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#KinesisFirehoseOutputDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.resource_arn
    import capo_kinesis_analytics.types.role_arn


class KinesisFirehoseOutputDescription(TypedDict, closed=True):
    resource_arn: NotRequired["capo_kinesis_analytics.types.resource_arn.ResourceARN"]
    """<p>Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.</p>"""
    role_arn: NotRequired["capo_kinesis_analytics.types.role_arn.RoleARN"]
    """<p>ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisFirehoseOutputDescription) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisFirehoseOutputDescription:
    out: KinesisFirehoseOutputDescription = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    return out
