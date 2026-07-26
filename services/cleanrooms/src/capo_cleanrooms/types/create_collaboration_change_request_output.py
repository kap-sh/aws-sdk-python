"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateCollaborationChangeRequestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_change_request


class CreateCollaborationChangeRequestOutput(TypedDict, closed=True):
    collaboration_change_request: (
        "capo_cleanrooms.types.collaboration_change_request.CollaborationChangeRequest"
    )


# --- restJson1 ser/de ---
def serialize_json(value: CreateCollaborationChangeRequestOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.collaboration_change_request

    out["collaborationChangeRequest"] = (
        capo_cleanrooms.types.collaboration_change_request.serialize_json(
            value["collaboration_change_request"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateCollaborationChangeRequestOutput:
    out: CreateCollaborationChangeRequestOutput = {}  # type: ignore[typeddict-item]
    if "collaborationChangeRequest" in data:
        import capo_cleanrooms.types.collaboration_change_request

        out["collaboration_change_request"] = (
            capo_cleanrooms.types.collaboration_change_request.deserialize_json(
                data["collaborationChangeRequest"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCollaborationChangeRequestOutput.collaboration_change_request required"
        )
    return out
