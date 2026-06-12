"""Generated from Smithy shape ``com.amazonaws.dlm#GetLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.policy_id


class GetLifecyclePolicyRequest(TypedDict):
    policy_id: "aws_sdk_dlm.types.policy_id.PolicyId"
    """<p>The identifier of the lifecycle policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLifecyclePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLifecyclePolicyRequest:
    out: GetLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
