"""Generated from Smithy shape ``com.amazonaws.medialive#StartMultiplexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class StartMultiplexRequest(TypedDict, closed=True):
    multiplex_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the multiplex."""


# --- restJson1 ser/de ---
def serialize_json(value: StartMultiplexRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartMultiplexRequest:
    out: StartMultiplexRequest = {}  # type: ignore[typeddict-item]
    return out
