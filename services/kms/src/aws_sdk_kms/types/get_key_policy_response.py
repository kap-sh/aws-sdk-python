"""Generated from Smithy shape ``com.amazonaws.kms#GetKeyPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.policy_name_type
    import aws_sdk_kms.types.policy_type


class GetKeyPolicyResponse(TypedDict):
    policy: NotRequired["aws_sdk_kms.types.policy_type.PolicyType"]
    """<p>A key policy document in JSON format.</p>"""
    policy_name: NotRequired["aws_sdk_kms.types.policy_name_type.PolicyNameType"]
    """<p>The name of the key policy. The only valid value is <code>default</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetKeyPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetKeyPolicyResponse:
    out: GetKeyPolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    return out
