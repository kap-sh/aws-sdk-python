"""Generated from Smithy shape ``com.amazonaws.transcribe#InputType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

InputType: TypeAlias = Literal[
    "REAL_TIME",
    "POST_CALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REAL_TIME",
        "POST_CALL",
    )
)


def serialize_aws_json_1_1(value: InputType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InputType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputType value: {data!r}")
    return cast(InputType, data)
