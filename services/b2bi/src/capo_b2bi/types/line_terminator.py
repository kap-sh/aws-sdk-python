"""Generated from Smithy shape ``com.amazonaws.b2bi#LineTerminator``."""

from typing import Literal, TypeAlias, cast

LineTerminator: TypeAlias = Literal[
    "CRLF",
    "LF",
    "CR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LineTerminator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LineTerminator:
    return cast(LineTerminator, data)
