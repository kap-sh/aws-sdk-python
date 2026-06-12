"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentDependencyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

ComponentDependencyType: TypeAlias = Literal[
    "HARD",
    "SOFT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HARD",
        "SOFT",
    )
)


def serialize_json(value: ComponentDependencyType) -> str:
    return value


def deserialize_json(data: str) -> ComponentDependencyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComponentDependencyType value: {data!r}")
    return cast(ComponentDependencyType, data)
