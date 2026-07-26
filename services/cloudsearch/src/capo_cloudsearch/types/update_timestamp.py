"""Generated from Smithy shape ``com.amazonaws.cloudsearch#UpdateTimestamp``."""

import datetime
from typing import TypeAlias

from capo_cloudsearch._protocol.xml import Element

UpdateTimestamp: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: UpdateTimestamp) -> str:
    return value.isoformat()


def from_query_text(text: str) -> UpdateTimestamp:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: UpdateTimestamp, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> UpdateTimestamp:
    return from_query_text(el.text or "")
