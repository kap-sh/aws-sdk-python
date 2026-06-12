"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#AccessDeniedReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service_data.errors import DeserializationError

AccessDeniedReason: TypeAlias = Literal[
    "IAM_AUTH",
    "DIRECTORY_AUTH",
    "DATA_DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM_AUTH",
        "DIRECTORY_AUTH",
        "DATA_DISABLED",
    )
)


def serialize_json(value: AccessDeniedReason) -> str:
    return value


def deserialize_json(data: str) -> AccessDeniedReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessDeniedReason value: {data!r}")
    return cast(AccessDeniedReason, data)
