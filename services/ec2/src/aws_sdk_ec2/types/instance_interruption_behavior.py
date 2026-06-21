"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceInterruptionBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

InstanceInterruptionBehavior: TypeAlias = Literal[
    "hibernate",
    "stop",
    "terminate",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InstanceInterruptionBehavior) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceInterruptionBehavior:
    return cast(InstanceInterruptionBehavior, text)


def serialize_ec2_query(
    value: InstanceInterruptionBehavior, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceInterruptionBehavior:
    return from_ec2_query_text(el.text or "")
