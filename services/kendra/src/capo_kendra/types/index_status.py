"""Generated from Smithy shape ``com.amazonaws.kendra#IndexStatus``."""

from typing import Literal, TypeAlias, cast

IndexStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
    "UPDATING",
    "SYSTEM_UPDATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IndexStatus:
    return cast(IndexStatus, data)
