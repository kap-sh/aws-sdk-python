"""Generated from Smithy shape ``com.amazonaws.medialive#H265RateControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Rate Control Mode"""
H265RateControlMode: TypeAlias = Literal[
    "CBR",
    "MULTIPLEX",
    "QVBR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CBR",
        "MULTIPLEX",
        "QVBR",
    )
)


def serialize_json(value: H265RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> H265RateControlMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265RateControlMode value: {data!r}")
    return cast(H265RateControlMode, data)
