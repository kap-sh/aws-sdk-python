"""Generated from Smithy shape ``com.amazonaws.ec2#HaStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

HaStatus: TypeAlias = Literal[
    "processing",
    "active",
    "standby",
    "invalid",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: HaStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> HaStatus:
    return cast(HaStatus, text)


def serialize_ec2_query(
    value: HaStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> HaStatus:
    return from_ec2_query_text(el.text or "")
