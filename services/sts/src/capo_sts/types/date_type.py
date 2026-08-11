"""Generated from Smithy shape ``com.amazonaws.sts#dateType``."""

import datetime
from typing import TypeAlias

from capo_sts._protocol.xml import Element

dateType: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: dateType) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def from_query_text(text: str) -> dateType:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(value: dateType, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> dateType:
    return from_query_text(el.text or "")
