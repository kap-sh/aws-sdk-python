"""Generated from Smithy shape ``com.amazonaws.applicationinsights#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "IGNORE",
    "RESOLVED",
    "PENDING",
    "RECURRING",
    "RECOVERING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Status) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Status:
    return cast(Status, data)
