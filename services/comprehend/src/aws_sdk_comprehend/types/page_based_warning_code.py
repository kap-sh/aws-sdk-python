"""Generated from Smithy shape ``com.amazonaws.comprehend#PageBasedWarningCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

PageBasedWarningCode: TypeAlias = Literal[
    "INFERENCING_PLAINTEXT_WITH_NATIVE_TRAINED_MODEL",
    "INFERENCING_NATIVE_DOCUMENT_WITH_PLAINTEXT_TRAINED_MODEL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFERENCING_PLAINTEXT_WITH_NATIVE_TRAINED_MODEL",
        "INFERENCING_NATIVE_DOCUMENT_WITH_PLAINTEXT_TRAINED_MODEL",
    )
)


def serialize_aws_json_1_1(value: PageBasedWarningCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PageBasedWarningCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PageBasedWarningCode value: {data!r}")
    return cast(PageBasedWarningCode, data)
