"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceGeneration``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

InstanceGeneration: TypeAlias = Literal[
    "current",
    "previous",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InstanceGeneration) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceGeneration:
    return cast(InstanceGeneration, text)


def serialize_ec2_query(
    value: InstanceGeneration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceGeneration:
    return from_ec2_query_text(el.text or "")
