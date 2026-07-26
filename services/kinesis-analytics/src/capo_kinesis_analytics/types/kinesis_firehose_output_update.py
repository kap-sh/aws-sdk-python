"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#KinesisFirehoseOutputUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.resource_arn
    import capo_kinesis_analytics.types.role_arn


class KinesisFirehoseOutputUpdate(TypedDict, closed=True):
    resource_arn_update: NotRequired[
        "capo_kinesis_analytics.types.resource_arn.ResourceARN"
    ]
    """<p>Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream to write to.</p>"""
    role_arn_update: NotRequired["capo_kinesis_analytics.types.role_arn.RoleARN"]
    """<p>ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisFirehoseOutputUpdate) -> dict:
    out: dict = {}
    if "resource_arn_update" in value:
        out["ResourceARNUpdate"] = value["resource_arn_update"]
    if "role_arn_update" in value:
        out["RoleARNUpdate"] = value["role_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisFirehoseOutputUpdate:
    out: KinesisFirehoseOutputUpdate = {}  # type: ignore[typeddict-item]
    if "ResourceARNUpdate" in data:
        out["resource_arn_update"] = data["ResourceARNUpdate"]
    if "RoleARNUpdate" in data:
        out["role_arn_update"] = data["RoleARNUpdate"]
    return out
