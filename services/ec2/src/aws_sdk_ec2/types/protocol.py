"""Generated from Smithy shape ``com.amazonaws.ec2#Protocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

Protocol: TypeAlias = Literal[
    "tcp",
    "udp",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: Protocol) -> str:
    return value


def from_ec2_query_text(text: str) -> Protocol:
    return cast(Protocol, text)


def serialize_ec2_query(
    value: Protocol, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> Protocol:
    return from_ec2_query_text(el.text or "")
