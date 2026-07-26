"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetStatusComparison``."""

from typing import Literal, TypeAlias, cast

CisTargetStatusComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: CisTargetStatusComparison) -> str:
    return value


def deserialize_json(data: str) -> CisTargetStatusComparison:
    return cast(CisTargetStatusComparison, data)
