"""Generated from Smithy shape ``com.amazonaws.mailmanager#ImportDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

ImportDataType: TypeAlias = Literal[
    "CSV",
    "JSON",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "JSON",
    )
)


def serialize_aws_json_1_0(value: ImportDataType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ImportDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportDataType value: {data!r}")
    return cast(ImportDataType, data)
