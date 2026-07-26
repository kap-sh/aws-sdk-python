"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationType``."""

from typing import Literal, TypeAlias, cast

ModelInvocationType: TypeAlias = Literal[
    "InvokeModel",
    "Converse",
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationType) -> str:
    return value


def deserialize_json(data: str) -> ModelInvocationType:
    return cast(ModelInvocationType, data)
