"""Generated from Smithy shape ``com.amazonaws.workmail#MemberType``."""

from typing import Literal, TypeAlias, cast

MemberType: TypeAlias = Literal[
    "GROUP",
    "USER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MemberType:
    return cast(MemberType, data)
