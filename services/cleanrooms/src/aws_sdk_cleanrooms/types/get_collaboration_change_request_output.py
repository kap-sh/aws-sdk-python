"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationChangeRequestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_change_request


class GetCollaborationChangeRequestOutput(TypedDict, closed=True):
    collaboration_change_request: "aws_sdk_cleanrooms.types.collaboration_change_request.CollaborationChangeRequest"
    """<p>The collaboration change request that was requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationChangeRequestOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.collaboration_change_request

    out["collaborationChangeRequest"] = (
        aws_sdk_cleanrooms.types.collaboration_change_request.serialize_json(
            value["collaboration_change_request"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetCollaborationChangeRequestOutput:
    out: GetCollaborationChangeRequestOutput = {}  # type: ignore[typeddict-item]
    if "collaborationChangeRequest" in data:
        import aws_sdk_cleanrooms.types.collaboration_change_request

        out["collaboration_change_request"] = (
            aws_sdk_cleanrooms.types.collaboration_change_request.deserialize_json(
                data["collaborationChangeRequest"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationChangeRequestOutput.collaboration_change_request required"
        )
    return out
