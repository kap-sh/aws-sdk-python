"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceLifecycleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

InstanceLifecycleType: TypeAlias = Literal[
    "spot",
    "scheduled",
    "capacity-block",
    "interruptible-capacity-reservation",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InstanceLifecycleType) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceLifecycleType:
    return cast(InstanceLifecycleType, text)


def serialize_ec2_query(
    value: InstanceLifecycleType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceLifecycleType:
    return from_ec2_query_text(el.text or "")
