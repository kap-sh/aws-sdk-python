"""Generated from Smithy shape ``com.amazonaws.quicksight#KPISparklineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

KPISparklineType: TypeAlias = Literal[
    "LINE",
    "AREA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINE",
        "AREA",
    )
)


def serialize_json(value: KPISparklineType) -> str:
    return value


def deserialize_json(data: str) -> KPISparklineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KPISparklineType value: {data!r}")
    return cast(KPISparklineType, data)
