"""Generated from Smithy shape ``com.amazonaws.ses#ArrivalDate``."""

import datetime
from typing import TypeAlias

from capo_ses._protocol.xml import Element

ArrivalDate: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: ArrivalDate) -> str:
    return value.isoformat()


def from_query_text(text: str) -> ArrivalDate:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: ArrivalDate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ArrivalDate:
    return from_query_text(el.text or "")
