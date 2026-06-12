"""Generated from Smithy shape ``com.amazonaws.medialive#H264TemporalAq``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Temporal Aq"""
H264TemporalAq: TypeAlias = Literal[
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


def serialize_json(value: H264TemporalAq) -> str:
    return value


def deserialize_json(data: str) -> H264TemporalAq:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264TemporalAq value: {data!r}")
    return cast(H264TemporalAq, data)
