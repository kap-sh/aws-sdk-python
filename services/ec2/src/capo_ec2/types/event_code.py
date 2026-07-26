"""Generated from Smithy shape ``com.amazonaws.ec2#EventCode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

EventCode: TypeAlias = Literal[
    "instance-reboot",
    "system-reboot",
    "system-maintenance",
    "instance-retirement",
    "instance-stop",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: EventCode) -> str:
    return value


def from_ec2_query_text(text: str) -> EventCode:
    return cast(EventCode, text)


def serialize_ec2_query(
    value: EventCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> EventCode:
    return from_ec2_query_text(el.text or "")
