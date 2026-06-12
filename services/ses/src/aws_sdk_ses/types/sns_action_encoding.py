"""Generated from Smithy shape ``com.amazonaws.ses#SNSActionEncoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

SNSActionEncoding: TypeAlias = Literal[
    "UTF-8",
    "Base64",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UTF-8",
        "Base64",
    )
)


def to_query_text(value: SNSActionEncoding) -> str:
    return value


def from_query_text(text: str) -> SNSActionEncoding:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SNSActionEncoding value: {text!r}")
    return cast(SNSActionEncoding, text)


def serialize_query(
    value: SNSActionEncoding, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SNSActionEncoding:
    return from_query_text(el.text or "")
