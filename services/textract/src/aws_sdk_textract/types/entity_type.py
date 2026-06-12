"""Generated from Smithy shape ``com.amazonaws.textract#EntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_textract.errors import DeserializationError

EntityType: TypeAlias = Literal[
    "KEY",
    "VALUE",
    "COLUMN_HEADER",
    "TABLE_TITLE",
    "TABLE_FOOTER",
    "TABLE_SECTION_TITLE",
    "TABLE_SUMMARY",
    "STRUCTURED_TABLE",
    "SEMI_STRUCTURED_TABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KEY",
        "VALUE",
        "COLUMN_HEADER",
        "TABLE_TITLE",
        "TABLE_FOOTER",
        "TABLE_SECTION_TITLE",
        "TABLE_SUMMARY",
        "STRUCTURED_TABLE",
        "SEMI_STRUCTURED_TABLE",
    )
)


def serialize_aws_json_1_1(value: EntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityType value: {data!r}")
    return cast(EntityType, data)
