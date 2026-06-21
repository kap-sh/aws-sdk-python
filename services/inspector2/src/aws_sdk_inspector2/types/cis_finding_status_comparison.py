"""Generated from Smithy shape ``com.amazonaws.inspector2#CisFindingStatusComparison``."""

from typing import Literal, TypeAlias, cast

CisFindingStatusComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: CisFindingStatusComparison) -> str:
    return value


def deserialize_json(data: str) -> CisFindingStatusComparison:
    return cast(CisFindingStatusComparison, data)
