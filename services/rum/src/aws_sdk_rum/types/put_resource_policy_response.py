"""Generated from Smithy shape ``com.amazonaws.rum#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_rum.types.policy_revision_id

class PutResourcePolicyResponse(TypedDict):
    policy_document: NotRequired["str"]
    """<p>The JSON policy document that you specified.</p>"""
    policy_revision_id: NotRequired["aws_sdk_rum.types.policy_revision_id.PolicyRevisionId"]
    """<p>The policy revision ID information that you specified.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy_document" in value:
        out["PolicyDocument"] = value["policy_document"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyDocument" in data:
        out["policy_document"] = data["PolicyDocument"]
    if "PolicyRevisionId" in data:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out