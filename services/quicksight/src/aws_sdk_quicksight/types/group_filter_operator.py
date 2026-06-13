"""Generated from Smithy shape ``com.amazonaws.quicksight#GroupFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

GroupFilterOperator: TypeAlias = Literal["StartsWith",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("StartsWith",))


def serialize_json(value: GroupFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> GroupFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupFilterOperator value: {data!r}")
    return cast(GroupFilterOperator, data)
