"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentParameterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

DocumentParameterType: TypeAlias = Literal[
    "String",
    "StringList",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "String",
        "StringList",
    )
)


def serialize_aws_json_1_1(value: DocumentParameterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentParameterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentParameterType value: {data!r}")
    return cast(DocumentParameterType, data)
