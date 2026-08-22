"""Generated from Smithy shape ``com.amazonaws.bedrock#IncludedModelsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.included_model_id

IncludedModelsList: TypeAlias = list[
    "capo_bedrock.types.included_model_id.IncludedModelId"
]


# --- restJson1 ser/de ---
def serialize_json(value: IncludedModelsList) -> list:
    return list(value)


def deserialize_json(data: list) -> IncludedModelsList:
    return [item for item in data if item is not None]
