"""Generated from Smithy shape ``com.amazonaws.ec2#ProtocolValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ProtocolValue: TypeAlias = Literal["gre",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ProtocolValue) -> str:
    return value


def from_ec2_query_text(text: str) -> ProtocolValue:
    return cast(ProtocolValue, text)


def serialize_ec2_query(
    value: ProtocolValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ProtocolValue:
    return from_ec2_query_text(el.text or "")
