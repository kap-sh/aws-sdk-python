"""Generated from Smithy shape ``com.amazonaws.firehose#DefaultDocumentIdFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

DefaultDocumentIdFormat: TypeAlias = Literal[
    "FIREHOSE_DEFAULT",
    "NO_DOCUMENT_ID",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIREHOSE_DEFAULT",
        "NO_DOCUMENT_ID",
    )
)


def serialize_aws_json_1_1(value: DefaultDocumentIdFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DefaultDocumentIdFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DefaultDocumentIdFormat value: {data!r}")
    return cast(DefaultDocumentIdFormat, data)
