"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#LambdaOutputDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.resource_arn
    import aws_sdk_kinesis_analytics_v2.types.role_arn


class LambdaOutputDescription(TypedDict, closed=True):
    resource_arn: "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the destination Lambda function.</p>"""
    role_arn: NotRequired["aws_sdk_kinesis_analytics_v2.types.role_arn.RoleARN"]
    """<p>The ARN of the IAM role that Kinesis Data Analytics can assume to write to the destination function.</p> <note> <p>Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaOutputDescription) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaOutputDescription:
    out: LambdaOutputDescription = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("LambdaOutputDescription.resource_arn required")
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    return out
