"""Generated from Smithy shape ``com.amazonaws.dynamodb#IndexStatus``."""

from typing import Literal, TypeAlias, cast

IndexStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "ACTIVE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IndexStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IndexStatus:
    return cast(IndexStatus, data)
