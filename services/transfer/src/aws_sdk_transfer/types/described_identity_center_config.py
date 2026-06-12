"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedIdentityCenterConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transfer.types.identity_center_application_arn
    import aws_sdk_transfer.types.identity_center_instance_arn
    import aws_sdk_transfer.types.role


class DescribedIdentityCenterConfig(TypedDict):
    application_arn: NotRequired[
        "aws_sdk_transfer.types.identity_center_application_arn.IdentityCenterApplicationArn"
    ]
    """<p>The Amazon Resource Name (ARN) for the IAM Identity Center application: this value is set automatically when you create your web app.</p>"""
    instance_arn: NotRequired[
        "aws_sdk_transfer.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) for the IAM Identity Center used for the web app.</p>"""
    role: NotRequired["aws_sdk_transfer.types.role.Role"]
    """<p>The IAM role in IAM Identity Center used for the web app.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedIdentityCenterConfig) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "role" in value:
        out["Role"] = value["role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedIdentityCenterConfig:
    out: DescribedIdentityCenterConfig = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    if "Role" in data:
        out["role"] = data["Role"]
    return out
