"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CustomSourceType``."""

from typing import Literal, TypeAlias, cast

CustomSourceType: TypeAlias = Literal[
    "IN_LINE",
    "S3_LOCATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomSourceType) -> str:
    return value


def deserialize_json(data: str) -> CustomSourceType:
    return cast(CustomSourceType, data)
