"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaInputPayloadEncodingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

LambdaInputPayloadEncodingType: TypeAlias = Literal[
    "json",
    "binary",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "json",
        "binary",
    )
)


def serialize_json(value: LambdaInputPayloadEncodingType) -> str:
    return value


def deserialize_json(data: str) -> LambdaInputPayloadEncodingType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LambdaInputPayloadEncodingType value: {data!r}"
        )
    return cast(LambdaInputPayloadEncodingType, data)
