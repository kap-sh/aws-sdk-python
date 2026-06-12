"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

RecordStatus: TypeAlias = Literal[
    "CREATED",
    "IN_PROGRESS",
    "IN_PROGRESS_IN_ERROR",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "IN_PROGRESS",
        "IN_PROGRESS_IN_ERROR",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: RecordStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordStatus value: {data!r}")
    return cast(RecordStatus, data)
