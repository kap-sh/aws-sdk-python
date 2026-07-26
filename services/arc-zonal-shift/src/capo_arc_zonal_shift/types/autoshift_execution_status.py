"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AutoshiftExecutionStatus``."""

from typing import Literal, TypeAlias, cast

AutoshiftExecutionStatus: TypeAlias = Literal[
    "ACTIVE",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoshiftExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoshiftExecutionStatus:
    return cast(AutoshiftExecutionStatus, data)
