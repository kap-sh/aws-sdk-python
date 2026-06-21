"""Generated from Smithy shape ``com.amazonaws.costexplorer#GenerationStatus``."""

from typing import Literal, TypeAlias, cast

GenerationStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "PROCESSING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GenerationStatus:
    return cast(GenerationStatus, data)
