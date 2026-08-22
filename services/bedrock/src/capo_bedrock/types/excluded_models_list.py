"""Generated from Smithy shape ``com.amazonaws.bedrock#ExcludedModelsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.excluded_model_id

ExcludedModelsList: TypeAlias = list[
    "capo_bedrock.types.excluded_model_id.ExcludedModelId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExcludedModelsList) -> list:
    return list(value)


def deserialize_json(data: list) -> ExcludedModelsList:
    return [item for item in data if item is not None]
