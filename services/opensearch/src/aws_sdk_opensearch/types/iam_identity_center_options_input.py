"""Generated from Smithy shape ``com.amazonaws.opensearch#IamIdentityCenterOptionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.arn
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.role_arn


class IamIdentityCenterOptionsInput(TypedDict):
    enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Specifies whether IAM Identity Center is enabled or disabled.</p>"""
    iam_identity_center_instance_arn: NotRequired["aws_sdk_opensearch.types.arn.ARN"]
    iam_role_for_identity_center_application_arn: NotRequired[
        "aws_sdk_opensearch.types.role_arn.RoleArn"
    ]
    """<p>The ARN of the IAM role associated with the IAM Identity Center application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamIdentityCenterOptionsInput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "iam_identity_center_instance_arn" in value:
        out["iamIdentityCenterInstanceArn"] = value["iam_identity_center_instance_arn"]
    if "iam_role_for_identity_center_application_arn" in value:
        out["iamRoleForIdentityCenterApplicationArn"] = value[
            "iam_role_for_identity_center_application_arn"
        ]
    return out


def deserialize_json(data: dict) -> IamIdentityCenterOptionsInput:
    out: IamIdentityCenterOptionsInput = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "iamIdentityCenterInstanceArn" in data:
        out["iam_identity_center_instance_arn"] = data["iamIdentityCenterInstanceArn"]
    if "iamRoleForIdentityCenterApplicationArn" in data:
        out["iam_role_for_identity_center_application_arn"] = data[
            "iamRoleForIdentityCenterApplicationArn"
        ]
    return out
