"""Generated from Smithy shape ``com.amazonaws.pcs#Size``."""

from typing import Literal, TypeAlias, cast

Size: TypeAlias = Literal[
    "SMALL",
    "MEDIUM",
    "LARGE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Size) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Size:
    return cast(Size, data)
