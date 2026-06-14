"""Generated from Smithy shape ``com.amazonaws.storagegateway#CacheReportFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_storage_gateway.errors import DeserializationError

CacheReportFilterName: TypeAlias = Literal[
    "UploadState",
    "UploadFailureReason",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UploadState",
        "UploadFailureReason",
    )
)


def serialize_aws_json_1_1(value: CacheReportFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CacheReportFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CacheReportFilterName value: {data!r}")
    return cast(CacheReportFilterName, data)
