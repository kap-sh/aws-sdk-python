"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Visibility``."""

from typing import Literal, TypeAlias, cast

Visibility: TypeAlias = Literal[
    "Full",
    "Limited",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Visibility) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Visibility:
    return cast(Visibility, data)
