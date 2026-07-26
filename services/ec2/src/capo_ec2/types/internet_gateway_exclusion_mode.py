"""Generated from Smithy shape ``com.amazonaws.ec2#InternetGatewayExclusionMode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

InternetGatewayExclusionMode: TypeAlias = Literal[
    "allow-bidirectional",
    "allow-egress",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InternetGatewayExclusionMode) -> str:
    return value


def from_ec2_query_text(text: str) -> InternetGatewayExclusionMode:
    return cast(InternetGatewayExclusionMode, text)


def serialize_ec2_query(
    value: InternetGatewayExclusionMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InternetGatewayExclusionMode:
    return from_ec2_query_text(el.text or "")
