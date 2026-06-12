"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups.errors import DeserializationError

GroupFilterName: TypeAlias = Literal[
    "resource-type",
    "configuration-type",
    "owner",
    "display-name",
    "criticality",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "resource-type",
        "configuration-type",
        "owner",
        "display-name",
        "criticality",
    )
)


def serialize_json(value: GroupFilterName) -> str:
    return value


def deserialize_json(data: str) -> GroupFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupFilterName value: {data!r}")
    return cast(GroupFilterName, data)
