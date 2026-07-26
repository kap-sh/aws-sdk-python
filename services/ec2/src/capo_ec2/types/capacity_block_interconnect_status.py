"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockInterconnectStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

CapacityBlockInterconnectStatus: TypeAlias = Literal[
    "ok",
    "impaired",
    "insufficient-data",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CapacityBlockInterconnectStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityBlockInterconnectStatus:
    return cast(CapacityBlockInterconnectStatus, text)


def serialize_ec2_query(
    value: CapacityBlockInterconnectStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityBlockInterconnectStatus:
    return from_ec2_query_text(el.text or "")
