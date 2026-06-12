"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeMultiplexRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DescribeMultiplexRequest(TypedDict):
    multiplex_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the multiplex."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMultiplexRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeMultiplexRequest:
    out: DescribeMultiplexRequest = {}  # type: ignore[typeddict-item]
    return out
