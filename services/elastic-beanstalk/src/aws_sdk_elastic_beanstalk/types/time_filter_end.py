"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#TimeFilterEnd``."""

import datetime
from typing import TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

TimeFilterEnd: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: TimeFilterEnd) -> str:
    return value.isoformat()


def from_query_text(text: str) -> TimeFilterEnd:
    return datetime.datetime.fromisoformat(text)


def serialize_query(
    value: TimeFilterEnd, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TimeFilterEnd:
    return from_query_text(el.text or "")
