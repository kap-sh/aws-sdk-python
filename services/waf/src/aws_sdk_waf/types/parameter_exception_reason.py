"""Generated from Smithy shape ``com.amazonaws.waf#ParameterExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf.errors import DeserializationError

ParameterExceptionReason: TypeAlias = Literal[
    "INVALID_OPTION",
    "ILLEGAL_COMBINATION",
    "ILLEGAL_ARGUMENT",
    "INVALID_TAG_KEY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_OPTION",
        "ILLEGAL_COMBINATION",
        "ILLEGAL_ARGUMENT",
        "INVALID_TAG_KEY",
    )
)


def serialize_aws_json_1_1(value: ParameterExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParameterExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParameterExceptionReason value: {data!r}")
    return cast(ParameterExceptionReason, data)
