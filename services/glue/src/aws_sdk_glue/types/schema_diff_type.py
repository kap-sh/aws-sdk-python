"""Generated from Smithy shape ``com.amazonaws.glue#SchemaDiffType``."""

from typing import Literal, TypeAlias, cast

SchemaDiffType: TypeAlias = Literal["SYNTAX_DIFF",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaDiffType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchemaDiffType:
    return cast(SchemaDiffType, data)
