"""Generated from Smithy shape ``com.amazonaws.dataexchange#DeleteEventActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string


class DeleteEventActionRequest(TypedDict, closed=True):
    event_action_id: "capo_dataexchange.types.__string.__string"
    """<p>The unique identifier for the event action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventActionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEventActionRequest:
    out: DeleteEventActionRequest = {}  # type: ignore[typeddict-item]
    return out
