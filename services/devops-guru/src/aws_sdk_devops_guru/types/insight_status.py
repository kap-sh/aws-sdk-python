"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

InsightStatus: TypeAlias = Literal[
    "ONGOING",
    "CLOSED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONGOING",
        "CLOSED",
    )
)


def serialize_json(value: InsightStatus) -> str:
    return value


def deserialize_json(data: str) -> InsightStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightStatus value: {data!r}")
    return cast(InsightStatus, data)
