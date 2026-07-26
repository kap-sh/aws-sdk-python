"""Generated from Smithy shape ``com.amazonaws.wafv2#Platform``."""

from typing import Literal, TypeAlias, cast

Platform: TypeAlias = Literal[
    "IOS",
    "ANDROID",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Platform) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Platform:
    return cast(Platform, data)
