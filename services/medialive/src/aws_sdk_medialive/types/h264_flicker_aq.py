"""Generated from Smithy shape ``com.amazonaws.medialive#H264FlickerAq``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Flicker Aq"""
H264FlickerAq: TypeAlias = Literal[
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


def serialize_json(value: H264FlickerAq) -> str:
    return value


def deserialize_json(data: str) -> H264FlickerAq:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264FlickerAq value: {data!r}")
    return cast(H264FlickerAq, data)
