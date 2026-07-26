"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ProfileTaskStatus``."""

from typing import Literal, TypeAlias, cast

ProfileTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CANCELED",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileTaskStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProfileTaskStatus:
    return cast(ProfileTaskStatus, data)
