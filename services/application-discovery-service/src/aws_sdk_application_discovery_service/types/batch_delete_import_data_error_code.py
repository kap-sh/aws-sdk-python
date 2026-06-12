"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteImportDataErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

BatchDeleteImportDataErrorCode: TypeAlias = Literal[
    "NOT_FOUND",
    "INTERNAL_SERVER_ERROR",
    "OVER_LIMIT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_FOUND",
        "INTERNAL_SERVER_ERROR",
        "OVER_LIMIT",
    )
)


def serialize_aws_json_1_1(value: BatchDeleteImportDataErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchDeleteImportDataErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchDeleteImportDataErrorCode value: {data!r}"
        )
    return cast(BatchDeleteImportDataErrorCode, data)
