"""Generated from Smithy shape ``com.amazonaws.ses#BulkEmailStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

BulkEmailStatus: TypeAlias = Literal[
    "Success",
    "MessageRejected",
    "MailFromDomainNotVerified",
    "ConfigurationSetDoesNotExist",
    "TemplateDoesNotExist",
    "AccountSuspended",
    "AccountThrottled",
    "AccountDailyQuotaExceeded",
    "InvalidSendingPoolName",
    "AccountSendingPaused",
    "ConfigurationSetSendingPaused",
    "InvalidParameterValue",
    "TransientFailure",
    "Failed",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Success",
        "MessageRejected",
        "MailFromDomainNotVerified",
        "ConfigurationSetDoesNotExist",
        "TemplateDoesNotExist",
        "AccountSuspended",
        "AccountThrottled",
        "AccountDailyQuotaExceeded",
        "InvalidSendingPoolName",
        "AccountSendingPaused",
        "ConfigurationSetSendingPaused",
        "InvalidParameterValue",
        "TransientFailure",
        "Failed",
    )
)


def to_query_text(value: BulkEmailStatus) -> str:
    return value


def from_query_text(text: str) -> BulkEmailStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BulkEmailStatus value: {text!r}")
    return cast(BulkEmailStatus, text)


def serialize_query(
    value: BulkEmailStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> BulkEmailStatus:
    return from_query_text(el.text or "")
