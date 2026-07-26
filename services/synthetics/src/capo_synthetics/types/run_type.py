"""Generated from Smithy shape ``com.amazonaws.synthetics#RunType``."""

from typing import Literal, TypeAlias, cast

RunType: TypeAlias = Literal[
    "CANARY_RUN",
    "DRY_RUN",
]


# --- restJson1 ser/de ---
def serialize_json(value: RunType) -> str:
    return value


def deserialize_json(data: str) -> RunType:
    return cast(RunType, data)
