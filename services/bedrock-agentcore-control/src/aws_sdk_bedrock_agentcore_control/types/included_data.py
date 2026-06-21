"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#IncludedData``."""

from typing import Literal, TypeAlias, cast

IncludedData: TypeAlias = Literal[
    "ALL_DATA",
    "METADATA_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: IncludedData) -> str:
    return value


def deserialize_json(data: str) -> IncludedData:
    return cast(IncludedData, data)
