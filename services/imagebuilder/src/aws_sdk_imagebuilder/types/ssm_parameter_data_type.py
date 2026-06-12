"""Generated from Smithy shape ``com.amazonaws.imagebuilder#SsmParameterDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

SsmParameterDataType: TypeAlias = Literal[
    "text",
    "aws:ec2:image",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "text",
        "aws:ec2:image",
    )
)


def serialize_json(value: SsmParameterDataType) -> str:
    return value


def deserialize_json(data: str) -> SsmParameterDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SsmParameterDataType value: {data!r}")
    return cast(SsmParameterDataType, data)
