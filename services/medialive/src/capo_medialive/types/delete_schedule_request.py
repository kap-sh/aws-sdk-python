"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DeleteScheduleRequest(TypedDict, closed=True):
    channel_id: "capo_medialive.types.__string.__string"
    """Id of the channel whose schedule is being deleted."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScheduleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteScheduleRequest:
    out: DeleteScheduleRequest = {}  # type: ignore[typeddict-item]
    return out
