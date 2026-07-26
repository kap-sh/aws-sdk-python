"""Generated from Smithy shape ``com.amazonaws.ecr#TagStatus``."""

from typing import Literal, TypeAlias, cast

TagStatus: TypeAlias = Literal[
    "TAGGED",
    "UNTAGGED",
    "ANY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TagStatus:
    return cast(TagStatus, data)
