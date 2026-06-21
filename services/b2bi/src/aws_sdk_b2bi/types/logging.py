"""Generated from Smithy shape ``com.amazonaws.b2bi#Logging``."""

from typing import Literal, TypeAlias, cast

Logging: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Logging) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Logging:
    return cast(Logging, data)
