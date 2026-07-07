"""Generated from Smithy shape ``com.amazonaws.dlm#CreateLifecyclePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.policy_id


class CreateLifecyclePolicyResponse(TypedDict, closed=True):
    policy_id: NotRequired["aws_sdk_dlm.types.policy_id.PolicyId"]
    """<p>The identifier of the lifecycle policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLifecyclePolicyResponse) -> dict:
    out: dict = {}
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    return out


def deserialize_json(data: dict) -> CreateLifecyclePolicyResponse:
    out: CreateLifecyclePolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyId" in data:
        out["policy_id"] = data["PolicyId"]
    return out
