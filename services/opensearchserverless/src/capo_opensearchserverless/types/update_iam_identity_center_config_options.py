"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateIamIdentityCenterConfigOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.iam_identity_center_group_attribute
    import capo_opensearchserverless.types.iam_identity_center_user_attribute


class UpdateIamIdentityCenterConfigOptions(TypedDict, closed=True):
    user_attribute: NotRequired[
        "capo_opensearchserverless.types.iam_identity_center_user_attribute.IamIdentityCenterUserAttribute"
    ]
    """<p>The user attribute for this IAM Identity Center integration. Defaults to <code>UserId</code>.</p>"""
    group_attribute: NotRequired[
        "capo_opensearchserverless.types.iam_identity_center_group_attribute.IamIdentityCenterGroupAttribute"
    ]
    """<p>The group attribute for this IAM Identity Center integration. Defaults to <code>GroupId</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateIamIdentityCenterConfigOptions) -> dict:
    out: dict = {}
    if "user_attribute" in value:
        out["userAttribute"] = value["user_attribute"]
    if "group_attribute" in value:
        out["groupAttribute"] = value["group_attribute"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateIamIdentityCenterConfigOptions:
    out: UpdateIamIdentityCenterConfigOptions = {}  # type: ignore[typeddict-item]
    if "userAttribute" in data:
        out["user_attribute"] = data["userAttribute"]
    if "groupAttribute" in data:
        out["group_attribute"] = data["groupAttribute"]
    return out
