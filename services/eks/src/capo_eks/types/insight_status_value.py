"""Generated from Smithy shape ``com.amazonaws.eks#InsightStatusValue``."""

from typing import Literal, TypeAlias, cast

InsightStatusValue: TypeAlias = Literal[
    "PASSING",
    "WARNING",
    "ERROR",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightStatusValue) -> str:
    return value


def deserialize_json(data: str) -> InsightStatusValue:
    return cast(InsightStatusValue, data)
