"""Generated from Smithy shape ``com.amazonaws.mediaconvert#SimulateReservedQueue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Enable this setting when you run a test job to estimate how many reserved transcoding slots (RTS) you need. When this is enabled, MediaConvert runs your job from an on-demand queue with similar performance to what you will see with one RTS in a reserved queue. This setting is disabled by default."""
SimulateReservedQueue: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: SimulateReservedQueue) -> str:
    return value


def deserialize_json(data: str) -> SimulateReservedQueue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SimulateReservedQueue value: {data!r}")
    return cast(SimulateReservedQueue, data)
