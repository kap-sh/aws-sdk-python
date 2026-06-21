"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ControlConditionType``."""

from typing import Literal, TypeAlias, cast

ControlConditionType: TypeAlias = Literal["CLOUDWATCH",]


# --- restJson1 ser/de ---
def serialize_json(value: ControlConditionType) -> str:
    return value


def deserialize_json(data: str) -> ControlConditionType:
    return cast(ControlConditionType, data)
