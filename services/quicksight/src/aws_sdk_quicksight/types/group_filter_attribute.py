"""Generated from Smithy shape ``com.amazonaws.quicksight#GroupFilterAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

GroupFilterAttribute: TypeAlias = Literal["GROUP_NAME",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GROUP_NAME",))


def serialize_json(value: GroupFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> GroupFilterAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupFilterAttribute value: {data!r}")
    return cast(GroupFilterAttribute, data)
