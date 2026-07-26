"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteMemberInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.collaboration_identifier


class DeleteMemberInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The unique identifier for the associated collaboration.</p>"""
    account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The account ID of the member to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMemberInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMemberInput:
    out: DeleteMemberInput = {}  # type: ignore[typeddict-item]
    return out
