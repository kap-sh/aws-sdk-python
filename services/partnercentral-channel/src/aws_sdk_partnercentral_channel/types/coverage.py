"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#Coverage``."""

from typing import Literal, TypeAlias, cast

Coverage: TypeAlias = Literal[
    "ENTIRE_ORGANIZATION",
    "MANAGEMENT_ACCOUNT_ONLY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Coverage) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Coverage:
    return cast(Coverage, data)
