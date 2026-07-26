"""Generated from Smithy shape ``com.amazonaws.wafregional#ParameterExceptionReason``."""

from typing import Literal, TypeAlias, cast

ParameterExceptionReason: TypeAlias = Literal[
    "INVALID_OPTION",
    "ILLEGAL_COMBINATION",
    "ILLEGAL_ARGUMENT",
    "INVALID_TAG_KEY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParameterExceptionReason:
    return cast(ParameterExceptionReason, data)
