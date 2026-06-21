"""Generated from Smithy shape ``com.amazonaws.backup#ConditionType``."""

from typing import Literal, TypeAlias, cast

ConditionType: TypeAlias = Literal["STRINGEQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionType) -> str:
    return value


def deserialize_json(data: str) -> ConditionType:
    return cast(ConditionType, data)
