"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#LaunchedAt``."""

import datetime
from typing import TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

LaunchedAt: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: LaunchedAt) -> str:
    return value.isoformat()


def from_query_text(text: str) -> LaunchedAt:
    return datetime.datetime.fromisoformat(text)


def serialize_query(
    value: LaunchedAt, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LaunchedAt:
    return from_query_text(el.text or "")
