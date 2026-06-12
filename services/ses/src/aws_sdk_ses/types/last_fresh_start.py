"""Generated from Smithy shape ``com.amazonaws.ses#LastFreshStart``."""

import datetime
from typing import TypeAlias

from aws_sdk_ses._protocol.xml import Element

LastFreshStart: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: LastFreshStart) -> str:
    return value.isoformat()


def from_query_text(text: str) -> LastFreshStart:
    return datetime.datetime.fromisoformat(text)


def serialize_query(
    value: LastFreshStart, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LastFreshStart:
    return from_query_text(el.text or "")
