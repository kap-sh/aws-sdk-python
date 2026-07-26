"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration


class GetCollaborationOutput(TypedDict, closed=True):
    collaboration: "capo_cleanrooms.types.collaboration.Collaboration"
    """<p>The entire collaboration for this identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.collaboration

    out["collaboration"] = capo_cleanrooms.types.collaboration.serialize_json(
        value["collaboration"]
    )
    return out


def deserialize_json(data: dict) -> GetCollaborationOutput:
    out: GetCollaborationOutput = {}  # type: ignore[typeddict-item]
    if "collaboration" in data:
        import capo_cleanrooms.types.collaboration

        out["collaboration"] = capo_cleanrooms.types.collaboration.deserialize_json(
            data["collaboration"]
        )
    else:
        raise DeserializationError("GetCollaborationOutput.collaboration required")
    return out
