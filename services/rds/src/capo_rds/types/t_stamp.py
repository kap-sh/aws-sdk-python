"""Generated from Smithy shape ``com.amazonaws.rds#TStamp``."""

import datetime
from typing import TypeAlias

from capo_rds._protocol.xml import Element

TStamp: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: TStamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def from_query_text(text: str) -> TStamp:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(value: TStamp, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TStamp:
    return from_query_text(el.text or "")
