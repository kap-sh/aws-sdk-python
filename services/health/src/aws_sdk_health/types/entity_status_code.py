"""Generated from Smithy shape ``com.amazonaws.health#entityStatusCode``."""

from typing import Literal, TypeAlias, cast

entityStatusCode: TypeAlias = Literal[
    "IMPAIRED",
    "UNIMPAIRED",
    "UNKNOWN",
    "PENDING",
    "RESOLVED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: entityStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> entityStatusCode:
    return cast(entityStatusCode, data)
