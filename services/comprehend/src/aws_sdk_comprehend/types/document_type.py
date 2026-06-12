"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

DocumentType: TypeAlias = Literal[
    "NATIVE_PDF",
    "SCANNED_PDF",
    "MS_WORD",
    "IMAGE",
    "PLAIN_TEXT",
    "TEXTRACT_DETECT_DOCUMENT_TEXT_JSON",
    "TEXTRACT_ANALYZE_DOCUMENT_JSON",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NATIVE_PDF",
        "SCANNED_PDF",
        "MS_WORD",
        "IMAGE",
        "PLAIN_TEXT",
        "TEXTRACT_DETECT_DOCUMENT_TEXT_JSON",
        "TEXTRACT_ANALYZE_DOCUMENT_JSON",
    )
)


def serialize_aws_json_1_1(value: DocumentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentType value: {data!r}")
    return cast(DocumentType, data)
