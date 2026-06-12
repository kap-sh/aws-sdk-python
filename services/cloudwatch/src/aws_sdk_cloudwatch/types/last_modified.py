"""Generated from Smithy shape ``com.amazonaws.cloudwatch#LastModified``."""

import datetime
from typing import TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

LastModified: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LastModified) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> LastModified:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- awsQuery ser/de ---
def to_query_text(value: LastModified) -> str:
    return value.isoformat()


def from_query_text(text: str) -> LastModified:
    return datetime.datetime.fromisoformat(text)


def serialize_query(
    value: LastModified, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LastModified:
    return from_query_text(el.text or "")
