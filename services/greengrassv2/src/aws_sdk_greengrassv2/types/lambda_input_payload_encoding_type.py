"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaInputPayloadEncodingType``."""

from typing import Literal, TypeAlias, cast

LambdaInputPayloadEncodingType: TypeAlias = Literal[
    "json",
    "binary",
]


# --- restJson1 ser/de ---
def serialize_json(value: LambdaInputPayloadEncodingType) -> str:
    return value


def deserialize_json(data: str) -> LambdaInputPayloadEncodingType:
    return cast(LambdaInputPayloadEncodingType, data)
