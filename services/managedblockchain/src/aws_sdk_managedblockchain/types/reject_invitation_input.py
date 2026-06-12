"""Generated from Smithy shape ``com.amazonaws.managedblockchain#RejectInvitationInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.resource_id_string


class RejectInvitationInput(TypedDict):
    invitation_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the invitation to reject.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectInvitationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RejectInvitationInput:
    out: RejectInvitationInput = {}  # type: ignore[typeddict-item]
    return out
