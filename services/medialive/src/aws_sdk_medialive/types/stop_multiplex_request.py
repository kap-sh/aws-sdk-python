"""Generated from Smithy shape ``com.amazonaws.medialive#StopMultiplexRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class StopMultiplexRequest(TypedDict):
    multiplex_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the multiplex."""


# --- restJson1 ser/de ---
def serialize_json(value: StopMultiplexRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopMultiplexRequest:
    out: StopMultiplexRequest = {}  # type: ignore[typeddict-item]
    return out
