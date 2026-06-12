"""Generated from Smithy shape ``com.amazonaws.ses#ReceiptFilterPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

ReceiptFilterPolicy: TypeAlias = Literal[
    "Block",
    "Allow",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Block",
        "Allow",
    )
)


def to_query_text(value: ReceiptFilterPolicy) -> str:
    return value


def from_query_text(text: str) -> ReceiptFilterPolicy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ReceiptFilterPolicy value: {text!r}")
    return cast(ReceiptFilterPolicy, text)


def serialize_query(
    value: ReceiptFilterPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReceiptFilterPolicy:
    return from_query_text(el.text or "")
