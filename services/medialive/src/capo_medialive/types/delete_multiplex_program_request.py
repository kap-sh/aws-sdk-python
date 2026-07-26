"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteMultiplexProgramRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DeleteMultiplexProgramRequest(TypedDict, closed=True):
    multiplex_id: "capo_medialive.types.__string.__string"
    """The ID of the multiplex that the program belongs to."""
    program_name: "capo_medialive.types.__string.__string"
    """The multiplex program name."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMultiplexProgramRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMultiplexProgramRequest:
    out: DeleteMultiplexProgramRequest = {}  # type: ignore[typeddict-item]
    return out
