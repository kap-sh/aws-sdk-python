"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Timestamp``."""

import datetime
from typing import TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

Timestamp: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Timestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> Timestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- awsQuery ser/de ---
def to_query_text(value: Timestamp) -> str:
    return value.isoformat()


def from_query_text(text: str) -> Timestamp:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: Timestamp, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Timestamp:
    return from_query_text(el.text or "")
