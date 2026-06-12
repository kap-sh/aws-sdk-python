"""Generated from Smithy shape ``com.amazonaws.servicecatalog#LastSyncStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

LastSyncStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: LastSyncStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LastSyncStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LastSyncStatus value: {data!r}")
    return cast(LastSyncStatus, data)
