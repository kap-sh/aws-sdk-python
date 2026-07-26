"""Generated from Smithy shape ``com.amazonaws.dax#ChangeType``."""

from typing import Literal, TypeAlias, cast

ChangeType: TypeAlias = Literal[
    "IMMEDIATE",
    "REQUIRES_REBOOT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChangeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChangeType:
    return cast(ChangeType, data)
