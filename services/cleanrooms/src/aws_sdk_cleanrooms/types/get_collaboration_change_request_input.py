"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationChangeRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_change_request_identifier
    import aws_sdk_cleanrooms.types.collaboration_identifier


class GetCollaborationChangeRequestInput(TypedDict, closed=True):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The identifier of the collaboration that the change request is made against.</p>"""
    change_request_identifier: "aws_sdk_cleanrooms.types.collaboration_change_request_identifier.CollaborationChangeRequestIdentifier"
    """<p>A unique identifier for the change request to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationChangeRequestInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCollaborationChangeRequestInput:
    out: GetCollaborationChangeRequestInput = {}  # type: ignore[typeddict-item]
    return out
