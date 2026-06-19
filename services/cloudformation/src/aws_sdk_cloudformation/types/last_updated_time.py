"""Generated from Smithy shape ``com.amazonaws.cloudformation#LastUpdatedTime``."""

import datetime
from typing import TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

LastUpdatedTime: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: LastUpdatedTime) -> str:
    return value.isoformat()


def from_query_text(text: str) -> LastUpdatedTime:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: LastUpdatedTime, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LastUpdatedTime:
    return from_query_text(el.text or "")
