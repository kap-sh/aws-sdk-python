"""Generated from Smithy shape ``com.amazonaws.textract#BlockType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_textract.errors import DeserializationError

BlockType: TypeAlias = Literal[
    "KEY_VALUE_SET",
    "PAGE",
    "LINE",
    "WORD",
    "TABLE",
    "CELL",
    "SELECTION_ELEMENT",
    "MERGED_CELL",
    "TITLE",
    "QUERY",
    "QUERY_RESULT",
    "SIGNATURE",
    "TABLE_TITLE",
    "TABLE_FOOTER",
    "LAYOUT_TEXT",
    "LAYOUT_TITLE",
    "LAYOUT_HEADER",
    "LAYOUT_FOOTER",
    "LAYOUT_SECTION_HEADER",
    "LAYOUT_PAGE_NUMBER",
    "LAYOUT_LIST",
    "LAYOUT_FIGURE",
    "LAYOUT_TABLE",
    "LAYOUT_KEY_VALUE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KEY_VALUE_SET",
        "PAGE",
        "LINE",
        "WORD",
        "TABLE",
        "CELL",
        "SELECTION_ELEMENT",
        "MERGED_CELL",
        "TITLE",
        "QUERY",
        "QUERY_RESULT",
        "SIGNATURE",
        "TABLE_TITLE",
        "TABLE_FOOTER",
        "LAYOUT_TEXT",
        "LAYOUT_TITLE",
        "LAYOUT_HEADER",
        "LAYOUT_FOOTER",
        "LAYOUT_SECTION_HEADER",
        "LAYOUT_PAGE_NUMBER",
        "LAYOUT_LIST",
        "LAYOUT_FIGURE",
        "LAYOUT_TABLE",
        "LAYOUT_KEY_VALUE",
    )
)


def serialize_aws_json_1_1(value: BlockType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlockType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlockType value: {data!r}")
    return cast(BlockType, data)
