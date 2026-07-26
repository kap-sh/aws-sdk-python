"""Generated from Smithy shape ``com.amazonaws.iot#DeletePolicyVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.policy_name
    import capo_iot.types.policy_version_id


class DeletePolicyVersionRequest(TypedDict, closed=True):
    policy_name: "capo_iot.types.policy_name.PolicyName"
    """<p>The name of the policy.</p>"""
    policy_version_id: "capo_iot.types.policy_version_id.PolicyVersionId"
    """<p>The policy version ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePolicyVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePolicyVersionRequest:
    out: DeletePolicyVersionRequest = {}  # type: ignore[typeddict-item]
    return out
