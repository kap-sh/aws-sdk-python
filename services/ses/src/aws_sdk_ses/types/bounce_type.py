"""Generated from Smithy shape ``com.amazonaws.ses#BounceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

BounceType: TypeAlias = Literal[
    "DoesNotExist",
    "MessageTooLarge",
    "ExceededQuota",
    "ContentRejected",
    "Undefined",
    "TemporaryFailure",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DoesNotExist",
        "MessageTooLarge",
        "ExceededQuota",
        "ContentRejected",
        "Undefined",
        "TemporaryFailure",
    )
)


def to_query_text(value: BounceType) -> str:
    return value


def from_query_text(text: str) -> BounceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BounceType value: {text!r}")
    return cast(BounceType, text)


def serialize_query(
    value: BounceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> BounceType:
    return from_query_text(el.text or "")
