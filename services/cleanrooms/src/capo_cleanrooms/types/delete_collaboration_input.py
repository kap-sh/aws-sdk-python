"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteCollaborationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_identifier


class DeleteCollaborationInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The identifier for the collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCollaborationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCollaborationInput:
    out: DeleteCollaborationInput = {}  # type: ignore[typeddict-item]
    return out
