"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeMultiplexProgramRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DescribeMultiplexProgramRequest(TypedDict, closed=True):
    multiplex_id: "capo_medialive.types.__string.__string"
    """The ID of the multiplex that the program belongs to."""
    program_name: "capo_medialive.types.__string.__string"
    """The name of the program."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMultiplexProgramRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeMultiplexProgramRequest:
    out: DescribeMultiplexProgramRequest = {}  # type: ignore[typeddict-item]
    return out
