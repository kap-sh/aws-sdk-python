"""Generated from Smithy shape ``com.amazonaws.sesv2#ScalingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

ScalingMode: TypeAlias = Literal[
    "STANDARD",
    "MANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "MANAGED",
    )
)


def serialize_json(value: ScalingMode) -> str:
    return value


def deserialize_json(data: str) -> ScalingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalingMode value: {data!r}")
    return cast(ScalingMode, data)
