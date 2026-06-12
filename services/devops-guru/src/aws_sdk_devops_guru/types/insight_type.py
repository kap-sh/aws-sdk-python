"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

InsightType: TypeAlias = Literal[
    "REACTIVE",
    "PROACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REACTIVE",
        "PROACTIVE",
    )
)


def serialize_json(value: InsightType) -> str:
    return value


def deserialize_json(data: str) -> InsightType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightType value: {data!r}")
    return cast(InsightType, data)
