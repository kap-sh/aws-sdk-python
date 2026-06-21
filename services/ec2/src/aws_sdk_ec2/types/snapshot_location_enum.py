"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotLocationEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

SnapshotLocationEnum: TypeAlias = Literal[
    "regional",
    "local",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SnapshotLocationEnum) -> str:
    return value


def from_ec2_query_text(text: str) -> SnapshotLocationEnum:
    return cast(SnapshotLocationEnum, text)


def serialize_ec2_query(
    value: SnapshotLocationEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SnapshotLocationEnum:
    return from_ec2_query_text(el.text or "")
