"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceProfileModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.inference_profile_model

InferenceProfileModels: TypeAlias = list[
    "capo_bedrock.types.inference_profile_model.InferenceProfileModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: InferenceProfileModels) -> list:
    import capo_bedrock.types.inference_profile_model

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.inference_profile_model.serialize_json(item))
    return out


def deserialize_json(data: list) -> InferenceProfileModels:
    import capo_bedrock.types.inference_profile_model

    out: InferenceProfileModels = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.inference_profile_model.deserialize_json(item))
    return out
