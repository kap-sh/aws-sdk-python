"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportViewType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

ExportViewType: TypeAlias = Literal[
    "NEW_IMAGE",
    "NEW_AND_OLD_IMAGES",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW_IMAGE",
        "NEW_AND_OLD_IMAGES",
    )
)


def serialize_aws_json_1_0(value: ExportViewType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportViewType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportViewType value: {data!r}")
    return cast(ExportViewType, data)
