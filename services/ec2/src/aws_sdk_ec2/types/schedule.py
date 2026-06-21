"""Generated from Smithy shape ``com.amazonaws.ec2#Schedule``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

Schedule: TypeAlias = Literal["hourly",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: Schedule) -> str:
    return value


def from_ec2_query_text(text: str) -> Schedule:
    return cast(Schedule, text)


def serialize_ec2_query(
    value: Schedule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> Schedule:
    return from_ec2_query_text(el.text or "")
