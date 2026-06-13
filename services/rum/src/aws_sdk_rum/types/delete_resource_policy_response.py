"""Generated from Smithy shape ``com.amazonaws.rum#DeleteResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rum.types.policy_revision_id


class DeleteResourcePolicyResponse(TypedDict):
    policy_revision_id: NotRequired[
        "aws_sdk_rum.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>The revision ID of the policy that was removed, if it had one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyResponse:
    out: DeleteResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyRevisionId" in data:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out
