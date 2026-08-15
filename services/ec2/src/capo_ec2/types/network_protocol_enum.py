"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkProtocolEnum``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

NetworkProtocolEnum: TypeAlias = Literal[
    "http",
    "https",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: NetworkProtocolEnum) -> str:
    return value


def from_ec2_query_text(text: str) -> NetworkProtocolEnum:
    return cast(NetworkProtocolEnum, text)


def serialize_ec2_query(
    value: NetworkProtocolEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> NetworkProtocolEnum:
    return from_ec2_query_text(el.text or "")
