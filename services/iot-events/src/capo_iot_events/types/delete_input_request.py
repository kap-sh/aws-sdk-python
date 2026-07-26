"""Generated from Smithy shape ``com.amazonaws.iotevents#DeleteInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.input_name


class DeleteInputRequest(TypedDict, closed=True):
    input_name: "capo_iot_events.types.input_name.InputName"
    """<p>The name of the input to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInputRequest:
    out: DeleteInputRequest = {}  # type: ignore[typeddict-item]
    return out
