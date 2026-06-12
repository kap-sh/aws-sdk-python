"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentReadAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

DocumentReadAction: TypeAlias = Literal[
    "TEXTRACT_DETECT_DOCUMENT_TEXT",
    "TEXTRACT_ANALYZE_DOCUMENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXTRACT_DETECT_DOCUMENT_TEXT",
        "TEXTRACT_ANALYZE_DOCUMENT",
    )
)


def serialize_aws_json_1_1(value: DocumentReadAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentReadAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentReadAction value: {data!r}")
    return cast(DocumentReadAction, data)
