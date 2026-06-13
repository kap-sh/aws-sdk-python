"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIVisualStandardLayoutType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

KPIVisualStandardLayoutType: TypeAlias = Literal[
    "CLASSIC",
    "VERTICAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLASSIC",
        "VERTICAL",
    )
)


def serialize_json(value: KPIVisualStandardLayoutType) -> str:
    return value


def deserialize_json(data: str) -> KPIVisualStandardLayoutType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KPIVisualStandardLayoutType value: {data!r}"
        )
    return cast(KPIVisualStandardLayoutType, data)
