"""Generated from Smithy shape ``com.amazonaws.inspector2#CisResultStatusComparison``."""

from typing import Literal, TypeAlias, cast

CisResultStatusComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: CisResultStatusComparison) -> str:
    return value


def deserialize_json(data: str) -> CisResultStatusComparison:
    return cast(CisResultStatusComparison, data)
