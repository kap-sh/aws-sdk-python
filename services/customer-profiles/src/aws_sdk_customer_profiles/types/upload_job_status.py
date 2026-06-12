"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UploadJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

UploadJobStatus: TypeAlias = Literal[
    "CREATED",
    "IN_PROGRESS",
    "PARTIALLY_SUCCEEDED",
    "SUCCEEDED",
    "FAILED",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "IN_PROGRESS",
        "PARTIALLY_SUCCEEDED",
        "SUCCEEDED",
        "FAILED",
        "STOPPED",
    )
)


def serialize_json(value: UploadJobStatus) -> str:
    return value


def deserialize_json(data: str) -> UploadJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UploadJobStatus value: {data!r}")
    return cast(UploadJobStatus, data)
