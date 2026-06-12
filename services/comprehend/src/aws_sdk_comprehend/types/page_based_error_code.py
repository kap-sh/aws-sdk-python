"""Generated from Smithy shape ``com.amazonaws.comprehend#PageBasedErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

PageBasedErrorCode: TypeAlias = Literal[
    "TEXTRACT_BAD_PAGE",
    "TEXTRACT_PROVISIONED_THROUGHPUT_EXCEEDED",
    "PAGE_CHARACTERS_EXCEEDED",
    "PAGE_SIZE_EXCEEDED",
    "INTERNAL_SERVER_ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXTRACT_BAD_PAGE",
        "TEXTRACT_PROVISIONED_THROUGHPUT_EXCEEDED",
        "PAGE_CHARACTERS_EXCEEDED",
        "PAGE_SIZE_EXCEEDED",
        "INTERNAL_SERVER_ERROR",
    )
)


def serialize_aws_json_1_1(value: PageBasedErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PageBasedErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PageBasedErrorCode value: {data!r}")
    return cast(PageBasedErrorCode, data)
