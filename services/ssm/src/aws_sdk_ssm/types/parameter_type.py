"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ParameterType: TypeAlias = Literal[
    "String",
    "StringList",
    "SecureString",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "String",
        "StringList",
        "SecureString",
    )
)


def serialize_aws_json_1_1(value: ParameterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParameterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParameterType value: {data!r}")
    return cast(ParameterType, data)
