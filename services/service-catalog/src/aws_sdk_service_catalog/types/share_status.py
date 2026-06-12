"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ShareStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ShareStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "IN_PROGRESS",
        "COMPLETED",
        "COMPLETED_WITH_ERRORS",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: ShareStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShareStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareStatus value: {data!r}")
    return cast(ShareStatus, data)
