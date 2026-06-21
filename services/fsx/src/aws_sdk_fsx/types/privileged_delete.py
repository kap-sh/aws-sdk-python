"""Generated from Smithy shape ``com.amazonaws.fsx#PrivilegedDelete``."""

from typing import Literal, TypeAlias, cast

PrivilegedDelete: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "PERMANENTLY_DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivilegedDelete) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PrivilegedDelete:
    return cast(PrivilegedDelete, data)
