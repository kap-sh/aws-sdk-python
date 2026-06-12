"""Generated from Smithy shape ``com.amazonaws.deadline#LicenseEndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

LicenseEndpointStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "DELETE_IN_PROGRESS",
    "READY",
    "NOT_READY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "DELETE_IN_PROGRESS",
        "READY",
        "NOT_READY",
    )
)


def serialize_json(value: LicenseEndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> LicenseEndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LicenseEndpointStatus value: {data!r}")
    return cast(LicenseEndpointStatus, data)
