"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceSizeType``."""

from typing import Literal, TypeAlias, cast

AudienceSizeType: TypeAlias = Literal[
    "ABSOLUTE",
    "PERCENTAGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudienceSizeType) -> str:
    return value


def deserialize_json(data: str) -> AudienceSizeType:
    return cast(AudienceSizeType, data)
