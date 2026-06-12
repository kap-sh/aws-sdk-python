"""Generated from Smithy shape ``com.amazonaws.resiliencehub#SuggestedChangesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.entity_description

SuggestedChangesList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.entity_description.EntityDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuggestedChangesList) -> list:
    return list(value)


def deserialize_json(data: list) -> SuggestedChangesList:
    return list(data)
