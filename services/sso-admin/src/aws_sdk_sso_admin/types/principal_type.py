"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PrincipalType``."""

from typing import Literal, TypeAlias, cast

PrincipalType: TypeAlias = Literal[
    "USER",
    "GROUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrincipalType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PrincipalType:
    return cast(PrincipalType, data)
