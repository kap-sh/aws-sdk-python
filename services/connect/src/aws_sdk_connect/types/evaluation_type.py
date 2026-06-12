"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationType: TypeAlias = Literal[
    "STANDARD",
    "CALIBRATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "CALIBRATION",
    )
)


def serialize_json(value: EvaluationType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationType value: {data!r}")
    return cast(EvaluationType, data)
