"""Generated from Smithy shape ``com.amazonaws.wafv2#PayloadType``."""

from typing import Literal, TypeAlias, cast

PayloadType: TypeAlias = Literal[
    "JSON",
    "FORM_ENCODED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PayloadType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PayloadType:
    return cast(PayloadType, data)
