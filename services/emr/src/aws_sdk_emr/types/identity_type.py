"""Generated from Smithy shape ``com.amazonaws.emr#IdentityType``."""

from typing import Literal, TypeAlias, cast

IdentityType: TypeAlias = Literal[
    "USER",
    "GROUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IdentityType:
    return cast(IdentityType, data)
