"""Generated from Smithy shape ``com.amazonaws.ec2#InternetGatewayBlockMode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

InternetGatewayBlockMode: TypeAlias = Literal[
    "off",
    "block-bidirectional",
    "block-ingress",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InternetGatewayBlockMode) -> str:
    return value


def from_ec2_query_text(text: str) -> InternetGatewayBlockMode:
    return cast(InternetGatewayBlockMode, text)


def serialize_ec2_query(
    value: InternetGatewayBlockMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InternetGatewayBlockMode:
    return from_ec2_query_text(el.text or "")
