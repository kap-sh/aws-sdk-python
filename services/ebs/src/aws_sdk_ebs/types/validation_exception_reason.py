"""Generated from Smithy shape ``com.amazonaws.ebs#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ebs.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "INVALID_CUSTOMER_KEY",
    "INVALID_PAGE_TOKEN",
    "INVALID_BLOCK_TOKEN",
    "INVALID_GRANT_TOKEN",
    "INVALID_SNAPSHOT_ID",
    "UNRELATED_SNAPSHOTS",
    "INVALID_BLOCK",
    "INVALID_CONTENT_ENCODING",
    "INVALID_TAG",
    "INVALID_DEPENDENCY_REQUEST",
    "INVALID_PARAMETER_VALUE",
    "INVALID_VOLUME_SIZE",
    "CONFLICTING_BLOCK_UPDATE",
    "INVALID_IMAGE_ID",
    "WRITE_REQUEST_TIMEOUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_CUSTOMER_KEY",
        "INVALID_PAGE_TOKEN",
        "INVALID_BLOCK_TOKEN",
        "INVALID_GRANT_TOKEN",
        "INVALID_SNAPSHOT_ID",
        "UNRELATED_SNAPSHOTS",
        "INVALID_BLOCK",
        "INVALID_CONTENT_ENCODING",
        "INVALID_TAG",
        "INVALID_DEPENDENCY_REQUEST",
        "INVALID_PARAMETER_VALUE",
        "INVALID_VOLUME_SIZE",
        "CONFLICTING_BLOCK_UPDATE",
        "INVALID_IMAGE_ID",
        "WRITE_REQUEST_TIMEOUT",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
