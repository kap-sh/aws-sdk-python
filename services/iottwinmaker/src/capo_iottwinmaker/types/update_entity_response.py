"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#UpdateEntityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.state
    import capo_iottwinmaker.types.timestamp


class UpdateEntityResponse(TypedDict, closed=True):
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the entity was last updated.</p>"""
    state: "capo_iottwinmaker.types.state.State"
    """<p>The current state of the entity update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEntityResponse) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> UpdateEntityResponse:
    out: UpdateEntityResponse = {}  # type: ignore[typeddict-item]
    if "updateDateTime" in data:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError("UpdateEntityResponse.update_date_time required")
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("UpdateEntityResponse.state required")
    return out
