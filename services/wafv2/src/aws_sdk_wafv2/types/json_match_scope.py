"""Generated from Smithy shape ``com.amazonaws.wafv2#JsonMatchScope``."""

from typing import Literal, TypeAlias, cast

JsonMatchScope: TypeAlias = Literal[
    "ALL",
    "KEY",
    "VALUE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JsonMatchScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JsonMatchScope:
    return cast(JsonMatchScope, data)
