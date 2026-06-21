"""Generated from Smithy shape ``com.amazonaws.lightsail#NameServersUpdateStateCode``."""

from typing import Literal, TypeAlias, cast

NameServersUpdateStateCode: TypeAlias = Literal[
    "SUCCEEDED",
    "PENDING",
    "FAILED",
    "STARTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NameServersUpdateStateCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NameServersUpdateStateCode:
    return cast(NameServersUpdateStateCode, data)
