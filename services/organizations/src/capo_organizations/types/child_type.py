"""Generated from Smithy shape ``com.amazonaws.organizations#ChildType``."""

from typing import Literal, TypeAlias, cast

ChildType: TypeAlias = Literal[
    "ACCOUNT",
    "ORGANIZATIONAL_UNIT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChildType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChildType:
    return cast(ChildType, data)
