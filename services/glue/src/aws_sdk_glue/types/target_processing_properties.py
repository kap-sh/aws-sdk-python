"""Generated from Smithy shape ``com.amazonaws.glue#TargetProcessingProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.string128
    import aws_sdk_glue.types.string2048


class TargetProcessingProperties(TypedDict):
    role_arn: NotRequired["aws_sdk_glue.types.string128.String128"]
    """<p>The IAM role to access the Glue database.</p>"""
    kms_arn: NotRequired["aws_sdk_glue.types.string2048.String2048"]
    """<p>The ARN of the KMS key used for encryption.</p>"""
    connection_name: NotRequired["aws_sdk_glue.types.string128.String128"]
    """<p>The Glue network connection to configure the Glue job running in the customer VPC.</p>"""
    event_bus_arn: NotRequired["aws_sdk_glue.types.string2048.String2048"]
    """<p>The ARN of an Eventbridge event bus to receive the integration status notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetProcessingProperties) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "kms_arn" in value:
        out["KmsArn"] = value["kms_arn"]
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetProcessingProperties:
    out: TargetProcessingProperties = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "KmsArn" in data:
        out["kms_arn"] = data["KmsArn"]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "EventBusArn" in data:
        out["event_bus_arn"] = data["EventBusArn"]
    return out
