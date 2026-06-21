"""Generated from Smithy shape ``com.amazonaws.ec2#SpotInstanceInterruptionBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

SpotInstanceInterruptionBehavior: TypeAlias = Literal[
    "hibernate",
    "stop",
    "terminate",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SpotInstanceInterruptionBehavior) -> str:
    return value


def from_ec2_query_text(text: str) -> SpotInstanceInterruptionBehavior:
    return cast(SpotInstanceInterruptionBehavior, text)


def serialize_ec2_query(
    value: SpotInstanceInterruptionBehavior, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SpotInstanceInterruptionBehavior:
    return from_ec2_query_text(el.text or "")
