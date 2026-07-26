"""Generated from Smithy shape ``com.amazonaws.ec2#StorageTier``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

StorageTier: TypeAlias = Literal[
    "archive",
    "standard",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: StorageTier) -> str:
    return value


def from_ec2_query_text(text: str) -> StorageTier:
    return cast(StorageTier, text)


def serialize_ec2_query(
    value: StorageTier, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> StorageTier:
    return from_ec2_query_text(el.text or "")
