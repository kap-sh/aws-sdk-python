"""Generated from Smithy shape ``com.amazonaws.b2bi#FileFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

FileFormat: TypeAlias = Literal[
    "XML",
    "JSON",
    "NOT_USED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "XML",
        "JSON",
        "NOT_USED",
    )
)


def serialize_aws_json_1_0(value: FileFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FileFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileFormat value: {data!r}")
    return cast(FileFormat, data)
