"""Generated from Smithy shape ``com.amazonaws.textract#AutoUpdate``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_textract.errors import DeserializationError

AutoUpdate: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: AutoUpdate) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoUpdate:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoUpdate value: {data!r}")
    return cast(AutoUpdate, data)
