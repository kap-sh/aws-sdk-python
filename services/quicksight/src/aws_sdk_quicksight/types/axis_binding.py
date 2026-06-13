"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisBinding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AxisBinding: TypeAlias = Literal[
    "PRIMARY_YAXIS",
    "SECONDARY_YAXIS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY_YAXIS",
        "SECONDARY_YAXIS",
    )
)


def serialize_json(value: AxisBinding) -> str:
    return value


def deserialize_json(data: str) -> AxisBinding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AxisBinding value: {data!r}")
    return cast(AxisBinding, data)
