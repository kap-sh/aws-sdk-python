"""Generated from Smithy shape ``com.amazonaws.ses#LastAttemptDate``."""

import datetime
from typing import TypeAlias

from capo_ses._protocol.xml import Element

LastAttemptDate: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: LastAttemptDate) -> str:
    return value.isoformat()


def from_query_text(text: str) -> LastAttemptDate:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: LastAttemptDate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LastAttemptDate:
    return from_query_text(el.text or "")
