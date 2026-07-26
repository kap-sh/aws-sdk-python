"""Generated from Smithy shape ``com.amazonaws.cloud9#MemberPermissions``."""

from typing import Literal, TypeAlias, cast

MemberPermissions: TypeAlias = Literal[
    "read-write",
    "read-only",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberPermissions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MemberPermissions:
    return cast(MemberPermissions, data)
