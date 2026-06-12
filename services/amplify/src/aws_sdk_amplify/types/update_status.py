"""Generated from Smithy shape ``com.amazonaws.amplify#UpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplify.errors import DeserializationError

UpdateStatus: TypeAlias = Literal[
    "REQUESTING_CERTIFICATE",
    "PENDING_VERIFICATION",
    "IMPORTING_CUSTOM_CERTIFICATE",
    "PENDING_DEPLOYMENT",
    "AWAITING_APP_CNAME",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUESTING_CERTIFICATE",
        "PENDING_VERIFICATION",
        "IMPORTING_CUSTOM_CERTIFICATE",
        "PENDING_DEPLOYMENT",
        "AWAITING_APP_CNAME",
        "UPDATE_COMPLETE",
        "UPDATE_FAILED",
    )
)


def serialize_json(value: UpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateStatus value: {data!r}")
    return cast(UpdateStatus, data)
