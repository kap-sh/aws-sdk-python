"""Generated from Smithy shape ``com.amazonaws.fsx#SnaplockType``."""

from typing import Literal, TypeAlias, cast

SnaplockType: TypeAlias = Literal[
    "COMPLIANCE",
    "ENTERPRISE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnaplockType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnaplockType:
    return cast(SnaplockType, data)
