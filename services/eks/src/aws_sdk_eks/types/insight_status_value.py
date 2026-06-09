"""Generated from Smithy shape ``com.amazonaws.eks#InsightStatusValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

InsightStatusValue: TypeAlias = Literal[
    "PASSING",
    "WARNING",
    "ERROR",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSING",
        "WARNING",
        "ERROR",
        "UNKNOWN",
    )
)


def serialize_json(value: InsightStatusValue) -> str:
    return value


def deserialize_json(data: str) -> InsightStatusValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightStatusValue value: {data!r}")
    return cast(InsightStatusValue, data)
