"""Generated from Smithy shape ``com.amazonaws.glue#PropertyType``."""

from typing import Literal, TypeAlias, cast

PropertyType: TypeAlias = Literal[
    "USER_INPUT",
    "SECRET",
    "READ_ONLY",
    "UNUSED",
    "SECRET_OR_USER_INPUT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropertyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PropertyType:
    return cast(PropertyType, data)
