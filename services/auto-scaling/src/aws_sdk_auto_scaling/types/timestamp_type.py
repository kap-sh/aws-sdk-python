"""Generated from Smithy shape ``com.amazonaws.autoscaling#TimestampType``."""

import datetime
from typing import TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

TimestampType: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: TimestampType) -> str:
    return value.isoformat()


def from_query_text(text: str) -> TimestampType:
    return datetime.datetime.fromisoformat(text)


def serialize_query(
    value: TimestampType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TimestampType:
    return from_query_text(el.text or "")
