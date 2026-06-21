"""Generated from Smithy shape ``com.amazonaws.wafv2#FallbackBehavior``."""

from typing import Literal, TypeAlias, cast

FallbackBehavior: TypeAlias = Literal[
    "MATCH",
    "NO_MATCH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FallbackBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FallbackBehavior:
    return cast(FallbackBehavior, data)
