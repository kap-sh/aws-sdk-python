"""Generated from Smithy shape ``com.amazonaws.ses#Timestamp``."""

import datetime
from typing import TypeAlias

from aws_sdk_ses._protocol.xml import Element

Timestamp: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: Timestamp) -> str:
    return value.isoformat()


def from_query_text(text: str) -> Timestamp:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: Timestamp, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Timestamp:
    return from_query_text(el.text or "")
