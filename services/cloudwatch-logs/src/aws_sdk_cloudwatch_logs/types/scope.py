"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Scope``."""

from typing import Literal, TypeAlias, cast

Scope: TypeAlias = Literal["ALL",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Scope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Scope:
    return cast(Scope, data)
