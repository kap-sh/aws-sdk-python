"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelOutputDataFormat``."""

from typing import Literal, TypeAlias, cast

ModelOutputDataFormat: TypeAlias = Literal[
    "TEXT_CSV",
    "APPLICATION_JSONLINES",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelOutputDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelOutputDataFormat:
    return cast(ModelOutputDataFormat, data)
