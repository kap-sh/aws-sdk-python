"""Generated from Smithy shape ``com.amazonaws.workspaces#Platform``."""

from typing import Literal, TypeAlias, cast

Platform: TypeAlias = Literal["WINDOWS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Platform) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Platform:
    return cast(Platform, data)
