"""Generated from Smithy shape ``com.amazonaws.ec2#HostRecovery``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

HostRecovery: TypeAlias = Literal[
    "on",
    "off",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: HostRecovery) -> str:
    return value


def from_ec2_query_text(text: str) -> HostRecovery:
    return cast(HostRecovery, text)


def serialize_ec2_query(
    value: HostRecovery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> HostRecovery:
    return from_ec2_query_text(el.text or "")
