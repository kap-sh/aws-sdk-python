"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.inference_type

InferenceTypeList: TypeAlias = list["capo_bedrock.types.inference_type.InferenceType"]


# --- restJson1 ser/de ---
def serialize_json(value: InferenceTypeList) -> list:
    import capo_bedrock.types.inference_type

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.inference_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> InferenceTypeList:
    import capo_bedrock.types.inference_type

    out: InferenceTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.inference_type.deserialize_json(item))
    return out
