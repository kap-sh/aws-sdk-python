"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeletionTime``."""

import datetime
from typing import TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

DeletionTime: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: DeletionTime) -> str:
    return value.isoformat()


def from_query_text(text: str) -> DeletionTime:
    return datetime.datetime.fromisoformat(text)


def serialize_query(
    value: DeletionTime, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DeletionTime:
    return from_query_text(el.text or "")
