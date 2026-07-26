"""Generated from Smithy shape ``com.amazonaws.iot#DeletePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.policy_name


class DeletePolicyRequest(TypedDict, closed=True):
    policy_name: "capo_iot.types.policy_name.PolicyName"
    """<p>The name of the policy to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePolicyRequest:
    out: DeletePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
