"""Generated from Smithy shape ``com.amazonaws.ebs#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
