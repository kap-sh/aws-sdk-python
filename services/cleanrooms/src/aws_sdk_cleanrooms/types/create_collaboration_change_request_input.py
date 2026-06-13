"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateCollaborationChangeRequestInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.change_input_list
    import aws_sdk_cleanrooms.types.collaboration_identifier


class CreateCollaborationChangeRequestInput(TypedDict):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The identifier of the collaboration that the change request is made against.</p>"""
    changes: "aws_sdk_cleanrooms.types.change_input_list.ChangeInputList"
    """<p>The list of changes to apply to the collaboration. Each change specifies the type of modification and the details of what should be changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCollaborationChangeRequestInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.change_input_list

    out["changes"] = aws_sdk_cleanrooms.types.change_input_list.serialize_json(
        value["changes"]
    )
    return out


def deserialize_json(data: dict) -> CreateCollaborationChangeRequestInput:
    out: CreateCollaborationChangeRequestInput = {}  # type: ignore[typeddict-item]
    if "changes" in data:
        import aws_sdk_cleanrooms.types.change_input_list

        out["changes"] = aws_sdk_cleanrooms.types.change_input_list.deserialize_json(
            data["changes"]
        )
    else:
        raise DeserializationError(
            "CreateCollaborationChangeRequestInput.changes required"
        )
    return out
