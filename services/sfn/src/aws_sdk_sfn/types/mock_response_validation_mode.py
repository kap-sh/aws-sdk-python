"""Generated from Smithy shape ``com.amazonaws.sfn#MockResponseValidationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

MockResponseValidationMode: TypeAlias = Literal[
    "STRICT",
    "PRESENT",
    "NONE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRICT",
        "PRESENT",
        "NONE",
    )
)


def serialize_aws_json_1_0(value: MockResponseValidationMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MockResponseValidationMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MockResponseValidationMode value: {data!r}"
        )
    return cast(MockResponseValidationMode, data)
