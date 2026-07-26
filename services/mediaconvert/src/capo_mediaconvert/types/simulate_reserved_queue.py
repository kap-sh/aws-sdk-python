"""Generated from Smithy shape ``com.amazonaws.mediaconvert#SimulateReservedQueue``."""

from typing import Literal, TypeAlias, cast

"""Enable this setting when you run a test job to estimate how many reserved transcoding slots (RTS) you need. When this is enabled, MediaConvert runs your job from an on-demand queue with similar performance to what you will see with one RTS in a reserved queue. This setting is disabled by default."""
SimulateReservedQueue: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SimulateReservedQueue) -> str:
    return value


def deserialize_json(data: str) -> SimulateReservedQueue:
    return cast(SimulateReservedQueue, data)
