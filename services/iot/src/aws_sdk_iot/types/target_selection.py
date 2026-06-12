"""Generated from Smithy shape ``com.amazonaws.iot#TargetSelection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

TargetSelection: TypeAlias = Literal[
    "CONTINUOUS",
    "SNAPSHOT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTINUOUS",
        "SNAPSHOT",
    )
)


def serialize_json(value: TargetSelection) -> str:
    return value


def deserialize_json(data: str) -> TargetSelection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetSelection value: {data!r}")
    return cast(TargetSelection, data)
