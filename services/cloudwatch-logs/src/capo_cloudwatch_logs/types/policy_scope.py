"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PolicyScope``."""

from typing import Literal, TypeAlias, cast

PolicyScope: TypeAlias = Literal[
    "ACCOUNT",
    "RESOURCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PolicyScope:
    return cast(PolicyScope, data)
