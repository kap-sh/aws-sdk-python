"""Generated from Smithy shape ``com.amazonaws.lightsail#ForwardValues``."""

from typing import Literal, TypeAlias, cast

ForwardValues: TypeAlias = Literal[
    "none",
    "allow-list",
    "all",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForwardValues) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ForwardValues:
    return cast(ForwardValues, data)
