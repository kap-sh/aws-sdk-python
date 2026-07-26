"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#VisualType``."""

from typing import Literal, TypeAlias, cast

VisualType: TypeAlias = Literal[
    "LINE",
    "BAR",
    "STACK",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VisualType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VisualType:
    return cast(VisualType, data)
