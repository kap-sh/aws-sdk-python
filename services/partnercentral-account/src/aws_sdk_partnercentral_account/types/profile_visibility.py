"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ProfileVisibility``."""

from typing import Literal, TypeAlias, cast

ProfileVisibility: TypeAlias = Literal[
    "PRIVATE",
    "PUBLIC",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileVisibility) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProfileVisibility:
    return cast(ProfileVisibility, data)
