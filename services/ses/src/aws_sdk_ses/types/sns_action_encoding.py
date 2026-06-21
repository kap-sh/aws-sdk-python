"""Generated from Smithy shape ``com.amazonaws.ses#SNSActionEncoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element

SNSActionEncoding: TypeAlias = Literal[
    "UTF-8",
    "Base64",
]


# --- awsQuery ser/de ---
def to_query_text(value: SNSActionEncoding) -> str:
    return value


def from_query_text(text: str) -> SNSActionEncoding:
    return cast(SNSActionEncoding, text)


def serialize_query(
    value: SNSActionEncoding, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SNSActionEncoding:
    return from_query_text(el.text or "")
