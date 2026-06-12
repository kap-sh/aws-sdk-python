"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyGroupMatchType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

HierarchyGroupMatchType: TypeAlias = Literal[
    "EXACT",
    "WITH_CHILD_GROUPS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXACT",
        "WITH_CHILD_GROUPS",
    )
)


def serialize_json(value: HierarchyGroupMatchType) -> str:
    return value


def deserialize_json(data: str) -> HierarchyGroupMatchType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HierarchyGroupMatchType value: {data!r}")
    return cast(HierarchyGroupMatchType, data)
