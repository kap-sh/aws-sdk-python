"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelModalityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.model_modality

ModelModalityList: TypeAlias = list["capo_bedrock.types.model_modality.ModelModality"]


# --- restJson1 ser/de ---
def serialize_json(value: ModelModalityList) -> list:
    import capo_bedrock.types.model_modality

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.model_modality.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModelModalityList:
    import capo_bedrock.types.model_modality

    out: ModelModalityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.model_modality.deserialize_json(item))
    return out
