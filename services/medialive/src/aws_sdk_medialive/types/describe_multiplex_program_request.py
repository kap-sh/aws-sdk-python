"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeMultiplexProgramRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DescribeMultiplexProgramRequest(TypedDict):
    multiplex_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the multiplex that the program belongs to."""
    program_name: "aws_sdk_medialive.types.__string.__string"
    """The name of the program."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMultiplexProgramRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeMultiplexProgramRequest:
    out: DescribeMultiplexProgramRequest = {}  # type: ignore[typeddict-item]
    return out
