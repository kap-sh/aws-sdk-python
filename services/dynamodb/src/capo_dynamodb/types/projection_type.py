"""Generated from Smithy shape ``com.amazonaws.dynamodb#ProjectionType``."""

from typing import Literal, TypeAlias, cast

ProjectionType: TypeAlias = Literal[
    "ALL",
    "KEYS_ONLY",
    "INCLUDE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProjectionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProjectionType:
    return cast(ProjectionType, data)
