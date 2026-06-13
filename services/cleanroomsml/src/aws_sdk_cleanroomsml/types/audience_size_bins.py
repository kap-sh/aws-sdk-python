"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceSizeBins``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_size_value

AudienceSizeBins: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.audience_size_value.AudienceSizeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudienceSizeBins) -> list:
    return list(value)


def deserialize_json(data: list) -> AudienceSizeBins:
    return list(data)
