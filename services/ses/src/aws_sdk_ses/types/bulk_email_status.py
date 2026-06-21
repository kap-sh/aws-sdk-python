"""Generated from Smithy shape ``com.amazonaws.ses#BulkEmailStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element

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
def to_query_text(value: BulkEmailStatus) -> str:
    return value


def from_query_text(text: str) -> BulkEmailStatus:
    return cast(BulkEmailStatus, text)


def serialize_query(
    value: BulkEmailStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> BulkEmailStatus:
    return from_query_text(el.text or "")
