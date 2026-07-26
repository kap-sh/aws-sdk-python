"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelInputDataFormat``."""

from typing import Literal, TypeAlias, cast

ModelInputDataFormat: TypeAlias = Literal[
    "TEXT_CSV",
    "APPLICATION_JSON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelInputDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelInputDataFormat:
    return cast(ModelInputDataFormat, data)
