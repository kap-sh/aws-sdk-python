"""Generated from Smithy shape ``com.amazonaws.workmail#AccessEffect``."""

from typing import Literal, TypeAlias, cast

AccessEffect: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessEffect) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessEffect:
    return cast(AccessEffect, data)
