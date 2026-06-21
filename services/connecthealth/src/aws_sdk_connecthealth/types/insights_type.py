"""Generated from Smithy shape ``com.amazonaws.connecthealth#InsightsType``."""

from typing import Literal, TypeAlias, cast

InsightsType: TypeAlias = Literal["PRE_VISIT",]


# --- restJson1 ser/de ---
def serialize_json(value: InsightsType) -> str:
    return value


def deserialize_json(data: str) -> InsightsType:
    return cast(InsightsType, data)
