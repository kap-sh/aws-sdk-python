"""Generated from Smithy shape ``com.amazonaws.ssm#Fault``."""

from typing import Literal, TypeAlias, cast

Fault: TypeAlias = Literal[
    "Client",
    "Server",
    "Unknown",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Fault) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Fault:
    return cast(Fault, data)
