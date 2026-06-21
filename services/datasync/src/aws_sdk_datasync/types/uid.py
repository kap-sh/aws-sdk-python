"""Generated from Smithy shape ``com.amazonaws.datasync#Uid``."""

from typing import Literal, TypeAlias, cast

Uid: TypeAlias = Literal[
    "NONE",
    "INT_VALUE",
    "NAME",
    "BOTH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Uid) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Uid:
    return cast(Uid, data)
