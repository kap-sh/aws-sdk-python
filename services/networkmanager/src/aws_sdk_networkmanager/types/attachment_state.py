"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

AttachmentState: TypeAlias = Literal[
    "REJECTED",
    "PENDING_ATTACHMENT_ACCEPTANCE",
    "CREATING",
    "FAILED",
    "AVAILABLE",
    "UPDATING",
    "PENDING_NETWORK_UPDATE",
    "PENDING_TAG_ACCEPTANCE",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REJECTED",
        "PENDING_ATTACHMENT_ACCEPTANCE",
        "CREATING",
        "FAILED",
        "AVAILABLE",
        "UPDATING",
        "PENDING_NETWORK_UPDATE",
        "PENDING_TAG_ACCEPTANCE",
        "DELETING",
    )
)


def serialize_json(value: AttachmentState) -> str:
    return value


def deserialize_json(data: str) -> AttachmentState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttachmentState value: {data!r}")
    return cast(AttachmentState, data)
