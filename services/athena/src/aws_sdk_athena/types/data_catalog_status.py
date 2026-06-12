"""Generated from Smithy shape ``com.amazonaws.athena#DataCatalogStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

DataCatalogStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_FAILED_CLEANUP_IN_PROGRESS",
    "CREATE_FAILED_CLEANUP_COMPLETE",
    "CREATE_FAILED_CLEANUP_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "CREATE_FAILED_CLEANUP_IN_PROGRESS",
        "CREATE_FAILED_CLEANUP_COMPLETE",
        "CREATE_FAILED_CLEANUP_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
    )
)


def serialize_aws_json_1_1(value: DataCatalogStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataCatalogStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataCatalogStatus value: {data!r}")
    return cast(DataCatalogStatus, data)
