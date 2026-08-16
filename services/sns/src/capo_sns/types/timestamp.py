"""Generated from Smithy shape ``com.amazonaws.sns#Timestamp``."""

import datetime
from typing import TypeAlias

from capo_sns._protocol.xml import Element

Timestamp: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: Timestamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def from_query_text(text: str) -> Timestamp:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: Timestamp, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Timestamp:
    return from_query_text(el.text or "")
