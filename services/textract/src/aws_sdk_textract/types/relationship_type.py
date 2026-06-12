"""Generated from Smithy shape ``com.amazonaws.textract#RelationshipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_textract.errors import DeserializationError

RelationshipType: TypeAlias = Literal[
    "VALUE",
    "CHILD",
    "COMPLEX_FEATURES",
    "MERGED_CELL",
    "TITLE",
    "ANSWER",
    "TABLE",
    "TABLE_TITLE",
    "TABLE_FOOTER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALUE",
        "CHILD",
        "COMPLEX_FEATURES",
        "MERGED_CELL",
        "TITLE",
        "ANSWER",
        "TABLE",
        "TABLE_TITLE",
        "TABLE_FOOTER",
    )
)


def serialize_aws_json_1_1(value: RelationshipType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelationshipType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelationshipType value: {data!r}")
    return cast(RelationshipType, data)
