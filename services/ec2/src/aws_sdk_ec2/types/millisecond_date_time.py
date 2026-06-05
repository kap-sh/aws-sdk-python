"""Generated from Smithy shape ``com.amazonaws.ec2#MillisecondDateTime``."""

import datetime
from typing import TypeAlias
from aws_sdk_ec2._protocol.xml import Element

MillisecondDateTime: TypeAlias = datetime.datetime


# --- ec2Query ser/de ---
def to_ec2_query_text(value: MillisecondDateTime) -> str:
    return value.isoformat()


def from_ec2_query_text(text: str) -> MillisecondDateTime:
    return datetime.datetime.fromisoformat(text)


def serialize_ec2_query(
    value: MillisecondDateTime, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> MillisecondDateTime:
    return from_ec2_query_text(el.text or "")
