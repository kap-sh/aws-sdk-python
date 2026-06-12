"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentReadMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

DocumentReadMode: TypeAlias = Literal[
    "SERVICE_DEFAULT",
    "FORCE_DOCUMENT_READ_ACTION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE_DEFAULT",
        "FORCE_DOCUMENT_READ_ACTION",
    )
)


def serialize_aws_json_1_1(value: DocumentReadMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentReadMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentReadMode value: {data!r}")
    return cast(DocumentReadMode, data)
