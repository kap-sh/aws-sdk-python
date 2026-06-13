"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteMemberInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.collaboration_identifier


class DeleteMemberInput(TypedDict):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The unique identifier for the associated collaboration.</p>"""
    account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The account ID of the member to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMemberInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMemberInput:
    out: DeleteMemberInput = {}  # type: ignore[typeddict-item]
    return out
