"""Generated from Smithy shape ``com.amazonaws.ec2#Affinity``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

Affinity: TypeAlias = Literal[
    "default",
    "host",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: Affinity) -> str:
    return value


def from_ec2_query_text(text: str) -> Affinity:
    return cast(Affinity, text)


def serialize_ec2_query(
    value: Affinity, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> Affinity:
    return from_ec2_query_text(el.text or "")
