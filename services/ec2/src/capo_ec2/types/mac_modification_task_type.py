"""Generated from Smithy shape ``com.amazonaws.ec2#MacModificationTaskType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

MacModificationTaskType: TypeAlias = Literal[
    "sip-modification",
    "volume-ownership-delegation",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: MacModificationTaskType) -> str:
    return value


def from_ec2_query_text(text: str) -> MacModificationTaskType:
    return cast(MacModificationTaskType, text)


def serialize_ec2_query(
    value: MacModificationTaskType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> MacModificationTaskType:
    return from_ec2_query_text(el.text or "")
