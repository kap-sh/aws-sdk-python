"""Generated from Smithy shape ``com.amazonaws.ec2#MillisecondDateTime``."""

import datetime
from typing import TypeAlias

from capo_ec2._protocol.xml import Element

MillisecondDateTime: TypeAlias = datetime.datetime


# --- ec2Query ser/de ---
def to_ec2_query_text(value: MillisecondDateTime) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def from_ec2_query_text(text: str) -> MillisecondDateTime:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_ec2_query(
    value: MillisecondDateTime, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> MillisecondDateTime:
    return from_ec2_query_text(el.text or "")
