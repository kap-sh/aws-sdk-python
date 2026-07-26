"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationRoleType``."""

from typing import Literal, TypeAlias, cast

ImpersonationRoleType: TypeAlias = Literal[
    "FULL_ACCESS",
    "READ_ONLY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpersonationRoleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImpersonationRoleType:
    return cast(ImpersonationRoleType, data)
