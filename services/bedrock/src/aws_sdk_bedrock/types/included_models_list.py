"""Generated from Smithy shape ``com.amazonaws.bedrock#IncludedModelsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.included_model_id

IncludedModelsList: TypeAlias = list[
    "aws_sdk_bedrock.types.included_model_id.IncludedModelId"
]


# --- restJson1 ser/de ---
def serialize_json(value: IncludedModelsList) -> list:
    return list(value)


def deserialize_json(data: list) -> IncludedModelsList:
    return list(data)
