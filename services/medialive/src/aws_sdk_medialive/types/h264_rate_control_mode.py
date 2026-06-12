"""Generated from Smithy shape ``com.amazonaws.medialive#H264RateControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Rate Control Mode"""
H264RateControlMode: TypeAlias = Literal[
    "CBR",
    "MULTIPLEX",
    "QVBR",
    "VBR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CBR",
        "MULTIPLEX",
        "QVBR",
        "VBR",
    )
)


def serialize_json(value: H264RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> H264RateControlMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264RateControlMode value: {data!r}")
    return cast(H264RateControlMode, data)
