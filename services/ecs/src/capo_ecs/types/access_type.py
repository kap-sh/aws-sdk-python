"""Generated from Smithy shape ``com.amazonaws.ecs#AccessType``."""

from typing import Literal, TypeAlias, cast

AccessType: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessType:
    return cast(AccessType, data)
