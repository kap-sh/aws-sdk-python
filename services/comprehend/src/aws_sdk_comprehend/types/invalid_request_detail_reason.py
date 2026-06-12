"""Generated from Smithy shape ``com.amazonaws.comprehend#InvalidRequestDetailReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

InvalidRequestDetailReason: TypeAlias = Literal[
    "DOCUMENT_SIZE_EXCEEDED",
    "UNSUPPORTED_DOC_TYPE",
    "PAGE_LIMIT_EXCEEDED",
    "TEXTRACT_ACCESS_DENIED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOCUMENT_SIZE_EXCEEDED",
        "UNSUPPORTED_DOC_TYPE",
        "PAGE_LIMIT_EXCEEDED",
        "TEXTRACT_ACCESS_DENIED",
    )
)


def serialize_aws_json_1_1(value: InvalidRequestDetailReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InvalidRequestDetailReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InvalidRequestDetailReason value: {data!r}"
        )
    return cast(InvalidRequestDetailReason, data)
