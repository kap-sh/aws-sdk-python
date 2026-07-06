"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_identifier


class GetCollaborationInput(TypedDict, closed=True):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The identifier for the collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCollaborationInput:
    out: GetCollaborationInput = {}  # type: ignore[typeddict-item]
    return out
