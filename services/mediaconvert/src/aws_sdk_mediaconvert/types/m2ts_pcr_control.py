"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsPcrControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When set to PCR_EVERY_PES_PACKET, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This is effective only when the PCR PID is the same as the video or audio elementary stream."""
M2tsPcrControl: TypeAlias = Literal[
    "PCR_EVERY_PES_PACKET",
    "CONFIGURED_PCR_PERIOD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PCR_EVERY_PES_PACKET",
        "CONFIGURED_PCR_PERIOD",
    )
)


def serialize_json(value: M2tsPcrControl) -> str:
    return value


def deserialize_json(data: str) -> M2tsPcrControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsPcrControl value: {data!r}")
    return cast(M2tsPcrControl, data)
