"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteMultiplexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DeleteMultiplexRequest(TypedDict, closed=True):
    multiplex_id: "capo_medialive.types.__string.__string"
    """The ID of the multiplex."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMultiplexRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMultiplexRequest:
    out: DeleteMultiplexRequest = {}  # type: ignore[typeddict-item]
    return out
