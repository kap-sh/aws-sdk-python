"""Generated from Smithy shape ``com.amazonaws.lightsail#AccessDirection``."""

from typing import Literal, TypeAlias, cast

AccessDirection: TypeAlias = Literal[
    "inbound",
    "outbound",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDirection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessDirection:
    return cast(AccessDirection, data)
