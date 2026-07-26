"""Generated from Smithy shape ``com.amazonaws.cloud9#Permissions``."""

from typing import Literal, TypeAlias, cast

Permissions: TypeAlias = Literal[
    "owner",
    "read-write",
    "read-only",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Permissions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Permissions:
    return cast(Permissions, data)
