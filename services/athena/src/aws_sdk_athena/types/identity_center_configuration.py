"""Generated from Smithy shape ``com.amazonaws.athena#IdentityCenterConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.boxed_boolean
    import aws_sdk_athena.types.identity_center_instance_arn


class IdentityCenterConfiguration(TypedDict):
    enable_identity_center: NotRequired[
        "aws_sdk_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Specifies whether the workgroup is IAM Identity Center supported.</p>"""
    identity_center_instance_arn: NotRequired[
        "aws_sdk_athena.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    ]
    """<p>The IAM Identity Center instance ARN that the workgroup associates to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityCenterConfiguration) -> dict:
    out: dict = {}
    if "enable_identity_center" in value:
        out["EnableIdentityCenter"] = value["enable_identity_center"]
    if "identity_center_instance_arn" in value:
        out["IdentityCenterInstanceArn"] = value["identity_center_instance_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityCenterConfiguration:
    out: IdentityCenterConfiguration = {}  # type: ignore[typeddict-item]
    if "EnableIdentityCenter" in data:
        out["enable_identity_center"] = data["EnableIdentityCenter"]
    if "IdentityCenterInstanceArn" in data:
        out["identity_center_instance_arn"] = data["IdentityCenterInstanceArn"]
    return out
