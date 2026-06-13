"""Generated from Smithy prelude shape ``smithy.api#Timestamp``."""

import datetime

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element


# --- awsQuery ser/de ---
def to_query_text(value: datetime.datetime) -> str:
    return value.isoformat()


def from_query_text(text: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(text)


def serialize_query(
    value: datetime.datetime, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> datetime.datetime:
    return from_query_text(el.text or "")
