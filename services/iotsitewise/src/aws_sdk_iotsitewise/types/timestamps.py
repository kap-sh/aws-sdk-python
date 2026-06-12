"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Timestamps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.time_in_nanos

Timestamps: TypeAlias = list["aws_sdk_iotsitewise.types.time_in_nanos.TimeInNanos"]


# --- restJson1 ser/de ---
def serialize_json(value: Timestamps) -> list:
    import aws_sdk_iotsitewise.types.time_in_nanos

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.time_in_nanos.serialize_json(item))
    return out


def deserialize_json(data: list) -> Timestamps:
    import aws_sdk_iotsitewise.types.time_in_nanos

    out: Timestamps = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.time_in_nanos.deserialize_json(item))
    return out
