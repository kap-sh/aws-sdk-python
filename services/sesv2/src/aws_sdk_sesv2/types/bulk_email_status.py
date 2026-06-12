"""Generated from Smithy shape ``com.amazonaws.sesv2#BulkEmailStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

BulkEmailStatus: TypeAlias = Literal[
    "SUCCESS",
    "MESSAGE_REJECTED",
    "MAIL_FROM_DOMAIN_NOT_VERIFIED",
    "CONFIGURATION_SET_NOT_FOUND",
    "TEMPLATE_NOT_FOUND",
    "ACCOUNT_SUSPENDED",
    "ACCOUNT_THROTTLED",
    "ACCOUNT_DAILY_QUOTA_EXCEEDED",
    "INVALID_SENDING_POOL_NAME",
    "ACCOUNT_SENDING_PAUSED",
    "CONFIGURATION_SET_SENDING_PAUSED",
    "INVALID_PARAMETER",
    "TRANSIENT_FAILURE",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "MESSAGE_REJECTED",
        "MAIL_FROM_DOMAIN_NOT_VERIFIED",
        "CONFIGURATION_SET_NOT_FOUND",
        "TEMPLATE_NOT_FOUND",
        "ACCOUNT_SUSPENDED",
        "ACCOUNT_THROTTLED",
        "ACCOUNT_DAILY_QUOTA_EXCEEDED",
        "INVALID_SENDING_POOL_NAME",
        "ACCOUNT_SENDING_PAUSED",
        "CONFIGURATION_SET_SENDING_PAUSED",
        "INVALID_PARAMETER",
        "TRANSIENT_FAILURE",
        "FAILED",
    )
)


def serialize_json(value: BulkEmailStatus) -> str:
    return value


def deserialize_json(data: str) -> BulkEmailStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BulkEmailStatus value: {data!r}")
    return cast(BulkEmailStatus, data)
