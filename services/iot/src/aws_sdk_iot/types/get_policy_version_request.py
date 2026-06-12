"""Generated from Smithy shape ``com.amazonaws.iot#GetPolicyVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_name
    import aws_sdk_iot.types.policy_version_id


class GetPolicyVersionRequest(TypedDict):
    policy_name: "aws_sdk_iot.types.policy_name.PolicyName"
    """<p>The name of the policy.</p>"""
    policy_version_id: "aws_sdk_iot.types.policy_version_id.PolicyVersionId"
    """<p>The policy version ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyVersionRequest:
    out: GetPolicyVersionRequest = {}  # type: ignore[typeddict-item]
    return out
