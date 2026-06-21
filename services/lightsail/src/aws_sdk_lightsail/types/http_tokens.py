"""Generated from Smithy shape ``com.amazonaws.lightsail#HttpTokens``."""

from typing import Literal, TypeAlias, cast

HttpTokens: TypeAlias = Literal[
    "optional",
    "required",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpTokens) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HttpTokens:
    return cast(HttpTokens, data)
