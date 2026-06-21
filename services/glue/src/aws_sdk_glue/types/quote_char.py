"""Generated from Smithy shape ``com.amazonaws.glue#QuoteChar``."""

from typing import Literal, TypeAlias, cast

QuoteChar: TypeAlias = Literal[
    "quote",
    "quillemet",
    "single_quote",
    "disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuoteChar) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QuoteChar:
    return cast(QuoteChar, data)
