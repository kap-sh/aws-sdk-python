"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#TimeFilterStart``."""

import datetime
from typing import TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

TimeFilterStart: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: TimeFilterStart) -> str:
    return value.isoformat()


def from_query_text(text: str) -> TimeFilterStart:
    return datetime.datetime.fromisoformat(text)


def serialize_query(
    value: TimeFilterStart, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TimeFilterStart:
    return from_query_text(el.text or "")
