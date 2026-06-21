"""Generated from Smithy shape ``com.amazonaws.ec2#InterruptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

InterruptionType: TypeAlias = Literal["adhoc",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InterruptionType) -> str:
    return value


def from_ec2_query_text(text: str) -> InterruptionType:
    return cast(InterruptionType, text)


def serialize_ec2_query(
    value: InterruptionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InterruptionType:
    return from_ec2_query_text(el.text or "")
