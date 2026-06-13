"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateCollaborationChangeRequestOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_change_request


class UpdateCollaborationChangeRequestOutput(TypedDict):
    collaboration_change_request: "aws_sdk_cleanrooms.types.collaboration_change_request.CollaborationChangeRequest"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCollaborationChangeRequestOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.collaboration_change_request

    out["collaborationChangeRequest"] = (
        aws_sdk_cleanrooms.types.collaboration_change_request.serialize_json(
            value["collaboration_change_request"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateCollaborationChangeRequestOutput:
    out: UpdateCollaborationChangeRequestOutput = {}  # type: ignore[typeddict-item]
    if "collaborationChangeRequest" in data:
        import aws_sdk_cleanrooms.types.collaboration_change_request

        out["collaboration_change_request"] = (
            aws_sdk_cleanrooms.types.collaboration_change_request.deserialize_json(
                data["collaborationChangeRequest"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCollaborationChangeRequestOutput.collaboration_change_request required"
        )
    return out
