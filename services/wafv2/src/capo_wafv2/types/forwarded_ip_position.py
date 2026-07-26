"""Generated from Smithy shape ``com.amazonaws.wafv2#ForwardedIPPosition``."""

from typing import Literal, TypeAlias, cast

ForwardedIPPosition: TypeAlias = Literal[
    "FIRST",
    "LAST",
    "ANY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForwardedIPPosition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ForwardedIPPosition:
    return cast(ForwardedIPPosition, data)
