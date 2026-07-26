"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#IncludeDeletedBackTo``."""

import datetime
from typing import TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

IncludeDeletedBackTo: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: IncludeDeletedBackTo) -> str:
    return value.isoformat()


def from_query_text(text: str) -> IncludeDeletedBackTo:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: IncludeDeletedBackTo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IncludeDeletedBackTo:
    return from_query_text(el.text or "")
