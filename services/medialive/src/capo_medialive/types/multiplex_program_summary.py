"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexProgramSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class MultiplexProgramSummary(TypedDict, closed=True):
    channel_id: NotRequired["capo_medialive.types.__string.__string"]
    """The MediaLive Channel associated with the program."""
    program_name: NotRequired["capo_medialive.types.__string.__string"]
    """The name of the multiplex program."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexProgramSummary) -> dict:
    out: dict = {}
    if "channel_id" in value:
        out["channelId"] = value["channel_id"]
    if "program_name" in value:
        out["programName"] = value["program_name"]
    return out


def deserialize_json(data: dict) -> MultiplexProgramSummary:
    out: MultiplexProgramSummary = {}  # type: ignore[typeddict-item]
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    if "programName" in data:
        out["program_name"] = data["programName"]
    return out
