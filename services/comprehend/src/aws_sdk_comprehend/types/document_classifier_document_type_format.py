"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierDocumentTypeFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

DocumentClassifierDocumentTypeFormat: TypeAlias = Literal[
    "PLAIN_TEXT_DOCUMENT",
    "SEMI_STRUCTURED_DOCUMENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PLAIN_TEXT_DOCUMENT",
        "SEMI_STRUCTURED_DOCUMENT",
    )
)


def serialize_aws_json_1_1(value: DocumentClassifierDocumentTypeFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentClassifierDocumentTypeFormat:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DocumentClassifierDocumentTypeFormat value: {data!r}"
        )
    return cast(DocumentClassifierDocumentTypeFormat, data)
