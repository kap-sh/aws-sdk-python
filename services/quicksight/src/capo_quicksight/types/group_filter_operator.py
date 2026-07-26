"""Generated from Smithy shape ``com.amazonaws.quicksight#GroupFilterOperator``."""

from typing import Literal, TypeAlias, cast

GroupFilterOperator: TypeAlias = Literal["StartsWith",]


# --- restJson1 ser/de ---
def serialize_json(value: GroupFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> GroupFilterOperator:
    return cast(GroupFilterOperator, data)
