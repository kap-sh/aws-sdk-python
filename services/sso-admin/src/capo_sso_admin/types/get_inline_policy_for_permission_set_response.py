"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetInlinePolicyForPermissionSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.permission_set_policy_document


class GetInlinePolicyForPermissionSetResponse(TypedDict, closed=True):
    inline_policy: NotRequired[
        "capo_sso_admin.types.permission_set_policy_document.PermissionSetPolicyDocument"
    ]
    """<p>The inline policy that is attached to the permission set.</p> <note> <p>For <code>Length Constraints</code>, if a valid ARN is provided for a permission set, it is possible for an empty inline policy to be returned.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInlinePolicyForPermissionSetResponse) -> dict:
    out: dict = {}
    if "inline_policy" in value:
        out["InlinePolicy"] = value["inline_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInlinePolicyForPermissionSetResponse:
    out: GetInlinePolicyForPermissionSetResponse = {}  # type: ignore[typeddict-item]
    if "InlinePolicy" in data:
        out["inline_policy"] = data["InlinePolicy"]
    return out
