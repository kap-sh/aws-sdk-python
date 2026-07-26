"""Generated from Smithy shape ``com.amazonaws.wafv2#BodyParsingFallbackBehavior``."""

from typing import Literal, TypeAlias, cast

BodyParsingFallbackBehavior: TypeAlias = Literal[
    "MATCH",
    "NO_MATCH",
    "EVALUATE_AS_STRING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BodyParsingFallbackBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BodyParsingFallbackBehavior:
    return cast(BodyParsingFallbackBehavior, data)
