"""Generated from Smithy shape ``com.amazonaws.kendra#ContentType``."""

from typing import Literal, TypeAlias, cast

ContentType: TypeAlias = Literal[
    "PDF",
    "HTML",
    "MS_WORD",
    "PLAIN_TEXT",
    "PPT",
    "RTF",
    "XML",
    "XSLT",
    "MS_EXCEL",
    "CSV",
    "JSON",
    "MD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContentType:
    return cast(ContentType, data)
