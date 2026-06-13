"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteCollaborationInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_identifier


class DeleteCollaborationInput(TypedDict):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The identifier for the collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCollaborationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCollaborationInput:
    out: DeleteCollaborationInput = {}  # type: ignore[typeddict-item]
    return out
