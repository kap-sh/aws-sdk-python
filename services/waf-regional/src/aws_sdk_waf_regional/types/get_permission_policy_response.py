"""Generated from Smithy shape ``com.amazonaws.wafregional#GetPermissionPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.policy_string


class GetPermissionPolicyResponse(TypedDict, closed=True):
    policy: NotRequired["aws_sdk_waf_regional.types.policy_string.PolicyString"]
    """<p>The IAM policy attached to the specified RuleGroup.</p>"""


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
