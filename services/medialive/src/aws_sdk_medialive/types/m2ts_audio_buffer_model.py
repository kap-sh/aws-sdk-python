"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsAudioBufferModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Audio Buffer Model"""
M2tsAudioBufferModel: TypeAlias = Literal[
    "ATSC",
    "DVB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATSC",
        "DVB",
    )
)


def serialize_json(value: M2tsAudioBufferModel) -> str:
    return value


def deserialize_json(data: str) -> M2tsAudioBufferModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsAudioBufferModel value: {data!r}")
    return cast(M2tsAudioBufferModel, data)
