"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateCollaborationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration


class UpdateCollaborationOutput(TypedDict, closed=True):
    collaboration: "aws_sdk_cleanrooms.types.collaboration.Collaboration"
    """<p>The entire collaboration that has been updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCollaborationOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.collaboration

    out["collaboration"] = aws_sdk_cleanrooms.types.collaboration.serialize_json(
        value["collaboration"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCollaborationOutput:
    out: UpdateCollaborationOutput = {}  # type: ignore[typeddict-item]
    if "collaboration" in data:
        import aws_sdk_cleanrooms.types.collaboration

        out["collaboration"] = aws_sdk_cleanrooms.types.collaboration.deserialize_json(
            data["collaboration"]
        )
    else:
        raise DeserializationError("UpdateCollaborationOutput.collaboration required")
    return out
