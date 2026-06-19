"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreatedTime``."""

import datetime
from typing import TypeAlias

from aws_sdk_elastic_load_balancing._protocol.xml import Element

CreatedTime: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: CreatedTime) -> str:
    return value.isoformat()


def from_query_text(text: str) -> CreatedTime:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: CreatedTime, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CreatedTime:
    return from_query_text(el.text or "")
