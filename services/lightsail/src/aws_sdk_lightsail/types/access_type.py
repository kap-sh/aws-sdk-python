"""Generated from Smithy shape ``com.amazonaws.lightsail#AccessType``."""

from typing import Literal, TypeAlias, cast

AccessType: TypeAlias = Literal[
    "public",
    "private",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessType:
    return cast(AccessType, data)
