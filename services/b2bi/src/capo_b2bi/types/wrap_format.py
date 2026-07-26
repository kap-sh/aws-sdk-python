"""Generated from Smithy shape ``com.amazonaws.b2bi#WrapFormat``."""

from typing import Literal, TypeAlias, cast

WrapFormat: TypeAlias = Literal[
    "SEGMENT",
    "ONE_LINE",
    "LINE_LENGTH",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WrapFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WrapFormat:
    return cast(WrapFormat, data)
