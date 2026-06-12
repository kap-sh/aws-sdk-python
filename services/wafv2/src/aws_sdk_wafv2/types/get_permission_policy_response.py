"""Generated from Smithy shape ``com.amazonaws.wafv2#GetPermissionPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.policy_string


class GetPermissionPolicyResponse(TypedDict):
    policy: NotRequired["aws_sdk_wafv2.types.policy_string.PolicyString"]
    """<p>The IAM policy that is attached to the specified rule group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPermissionPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPermissionPolicyResponse:
    out: GetPermissionPolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
