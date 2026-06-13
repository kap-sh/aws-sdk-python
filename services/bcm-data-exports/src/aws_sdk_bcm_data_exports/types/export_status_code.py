"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExportStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_data_exports.errors import DeserializationError

ExportStatusCode: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
    )
)


def serialize_aws_json_1_1(value: ExportStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportStatusCode value: {data!r}")
    return cast(ExportStatusCode, data)
