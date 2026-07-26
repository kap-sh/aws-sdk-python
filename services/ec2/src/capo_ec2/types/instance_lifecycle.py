"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceLifecycle``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

InstanceLifecycle: TypeAlias = Literal[
    "spot",
    "on-demand",
    "interruptible-capacity-reservation",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InstanceLifecycle) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceLifecycle:
    return cast(InstanceLifecycle, text)


def serialize_ec2_query(
    value: InstanceLifecycle, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceLifecycle:
    return from_ec2_query_text(el.text or "")
