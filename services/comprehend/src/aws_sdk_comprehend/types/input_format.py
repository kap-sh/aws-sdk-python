"""Generated from Smithy shape ``com.amazonaws.comprehend#InputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

InputFormat: TypeAlias = Literal[
    "ONE_DOC_PER_FILE",
    "ONE_DOC_PER_LINE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONE_DOC_PER_FILE",
        "ONE_DOC_PER_LINE",
    )
)


def serialize_aws_json_1_1(value: InputFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputFormat value: {data!r}")
    return cast(InputFormat, data)
