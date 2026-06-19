"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#LastModifiedTime``."""

import datetime
from typing import TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

LastModifiedTime: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: LastModifiedTime) -> str:
    return value.isoformat()


def from_query_text(text: str) -> LastModifiedTime:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: LastModifiedTime, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LastModifiedTime:
    return from_query_text(el.text or "")
