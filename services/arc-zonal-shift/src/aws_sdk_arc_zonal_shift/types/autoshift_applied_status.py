"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AutoshiftAppliedStatus``."""

from typing import Literal, TypeAlias, cast

AutoshiftAppliedStatus: TypeAlias = Literal[
    "APPLIED",
    "NOT_APPLIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoshiftAppliedStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoshiftAppliedStatus:
    return cast(AutoshiftAppliedStatus, data)
