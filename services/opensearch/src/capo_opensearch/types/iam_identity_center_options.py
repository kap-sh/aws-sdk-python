"""Generated from Smithy shape ``com.amazonaws.opensearch#IamIdentityCenterOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn
    import capo_opensearch.types.boolean
    import capo_opensearch.types.role_arn


class IamIdentityCenterOptions(TypedDict, closed=True):
    enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Indicates whether IAM Identity Center is enabled for the OpenSearch application.</p>"""
    iam_identity_center_instance_arn: NotRequired["capo_opensearch.types.arn.ARN"]
    iam_role_for_identity_center_application_arn: NotRequired[
        "capo_opensearch.types.role_arn.RoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role assigned to the IAM Identity Center application for the OpenSearch application.</p>"""
    iam_identity_center_application_arn: NotRequired["capo_opensearch.types.arn.ARN"]


# --- restJson1 ser/de ---
def serialize_json(value: IamIdentityCenterOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "iam_identity_center_instance_arn" in value:
        out["iamIdentityCenterInstanceArn"] = value["iam_identity_center_instance_arn"]
    if "iam_role_for_identity_center_application_arn" in value:
        out["iamRoleForIdentityCenterApplicationArn"] = value[
            "iam_role_for_identity_center_application_arn"
        ]
    if "iam_identity_center_application_arn" in value:
        out["iamIdentityCenterApplicationArn"] = value[
            "iam_identity_center_application_arn"
        ]
    return out


def deserialize_json(data: dict) -> IamIdentityCenterOptions:
    out: IamIdentityCenterOptions = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "iamIdentityCenterInstanceArn" in data:
        out["iam_identity_center_instance_arn"] = data["iamIdentityCenterInstanceArn"]
    if "iamRoleForIdentityCenterApplicationArn" in data:
        out["iam_role_for_identity_center_application_arn"] = data[
            "iamRoleForIdentityCenterApplicationArn"
        ]
    if "iamIdentityCenterApplicationArn" in data:
        out["iam_identity_center_application_arn"] = data[
            "iamIdentityCenterApplicationArn"
        ]
    return out
