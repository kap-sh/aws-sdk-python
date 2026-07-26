"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexProgramChannelDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string_min1


class MultiplexProgramChannelDestinationSettings(TypedDict, closed=True):
    multiplex_id: NotRequired["capo_medialive.types.__string_min1.__stringMin1"]
    """The ID of the Multiplex that the encoder is providing output to. You do not need to specify the individual inputs to the Multiplex; MediaLive will handle the connection of the two MediaLive pipelines to the two Multiplex instances. The Multiplex must be in the same region as the Channel."""
    program_name: NotRequired["capo_medialive.types.__string_min1.__stringMin1"]
    """The program name of the Multiplex program that the encoder is providing output to."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexProgramChannelDestinationSettings) -> dict:
    out: dict = {}
    if "multiplex_id" in value:
        out["multiplexId"] = value["multiplex_id"]
    if "program_name" in value:
        out["programName"] = value["program_name"]
    return out


def deserialize_json(data: dict) -> MultiplexProgramChannelDestinationSettings:
    out: MultiplexProgramChannelDestinationSettings = {}  # type: ignore[typeddict-item]
    if "multiplexId" in data:
        out["multiplex_id"] = data["multiplexId"]
    if "programName" in data:
        out["program_name"] = data["programName"]
    return out
