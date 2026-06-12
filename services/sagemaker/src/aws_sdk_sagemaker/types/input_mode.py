"""Generated from Smithy shape ``com.amazonaws.sagemaker#InputMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

InputMode: TypeAlias = Literal[
    "Pipe",
    "File",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pipe",
        "File",
    )
)


def serialize_aws_json_1_1(value: InputMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InputMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputMode value: {data!r}")
    return cast(InputMode, data)
