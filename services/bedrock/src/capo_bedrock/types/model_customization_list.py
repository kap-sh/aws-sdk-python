"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelCustomizationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.model_customization

ModelCustomizationList: TypeAlias = list[
    "capo_bedrock.types.model_customization.ModelCustomization"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelCustomizationList) -> list:
    import capo_bedrock.types.model_customization

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.model_customization.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModelCustomizationList:
    import capo_bedrock.types.model_customization

    out: ModelCustomizationList = []
    for item in data:
        out.append(capo_bedrock.types.model_customization.deserialize_json(item))
    return out
