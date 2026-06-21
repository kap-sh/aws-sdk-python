"""Generated from Smithy shape ``com.amazonaws.textract#RelationshipType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: RelationshipType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelationshipType:
    return cast(RelationshipType, data)
