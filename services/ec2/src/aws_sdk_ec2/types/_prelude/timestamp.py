"""Generated from Smithy prelude shape ``smithy.api#Timestamp``."""

import datetime

from aws_sdk_ec2._protocol.xml import Element


# --- ec2Query ser/de ---
def to_ec2_query_text(value: datetime.datetime) -> str:
    return value.isoformat()


def from_ec2_query_text(text: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(text)


def serialize_ec2_query(
    value: datetime.datetime, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> datetime.datetime:
    return from_ec2_query_text(el.text or "")
