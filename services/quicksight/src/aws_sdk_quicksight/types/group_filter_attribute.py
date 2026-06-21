"""Generated from Smithy shape ``com.amazonaws.quicksight#GroupFilterAttribute``."""

from typing import Literal, TypeAlias, cast

GroupFilterAttribute: TypeAlias = Literal["GROUP_NAME",]


# --- restJson1 ser/de ---
def serialize_json(value: GroupFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> GroupFilterAttribute:
    return cast(GroupFilterAttribute, data)
