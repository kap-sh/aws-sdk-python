"""Generated from Smithy shape ``com.amazonaws.lakeformation#OptimizerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

OptimizerType: TypeAlias = Literal[
    "COMPACTION",
    "GARBAGE_COLLECTION",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPACTION",
        "GARBAGE_COLLECTION",
        "ALL",
    )
)


def serialize_json(value: OptimizerType) -> str:
    return value


def deserialize_json(data: str) -> OptimizerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OptimizerType value: {data!r}")
    return cast(OptimizerType, data)
