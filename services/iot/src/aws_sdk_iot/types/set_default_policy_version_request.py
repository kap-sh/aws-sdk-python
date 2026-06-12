"""Generated from Smithy shape ``com.amazonaws.iot#SetDefaultPolicyVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_name
    import aws_sdk_iot.types.policy_version_id


class SetDefaultPolicyVersionRequest(TypedDict):
    policy_name: "aws_sdk_iot.types.policy_name.PolicyName"
    """<p>The policy name.</p>"""
    policy_version_id: "aws_sdk_iot.types.policy_version_id.PolicyVersionId"
    """<p>The policy version ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetDefaultPolicyVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SetDefaultPolicyVersionRequest:
    out: SetDefaultPolicyVersionRequest = {}  # type: ignore[typeddict-item]
    return out
