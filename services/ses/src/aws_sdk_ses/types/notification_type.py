"""Generated from Smithy shape ``com.amazonaws.ses#NotificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

NotificationType: TypeAlias = Literal[
    "Bounce",
    "Complaint",
    "Delivery",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Bounce",
        "Complaint",
        "Delivery",
    )
)


def to_query_text(value: NotificationType) -> str:
    return value


def from_query_text(text: str) -> NotificationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown NotificationType value: {text!r}")
    return cast(NotificationType, text)


def serialize_query(
    value: NotificationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> NotificationType:
    return from_query_text(el.text or "")
