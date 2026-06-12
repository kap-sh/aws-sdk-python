"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierDataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

DocumentClassifierDataFormat: TypeAlias = Literal[
    "COMPREHEND_CSV",
    "AUGMENTED_MANIFEST",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPREHEND_CSV",
        "AUGMENTED_MANIFEST",
    )
)


def serialize_aws_json_1_1(value: DocumentClassifierDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentClassifierDataFormat:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DocumentClassifierDataFormat value: {data!r}"
        )
    return cast(DocumentClassifierDataFormat, data)
