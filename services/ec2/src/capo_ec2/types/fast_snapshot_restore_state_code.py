"""Generated from Smithy shape ``com.amazonaws.ec2#FastSnapshotRestoreStateCode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

FastSnapshotRestoreStateCode: TypeAlias = Literal[
    "enabling",
    "optimizing",
    "enabled",
    "disabling",
    "disabled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FastSnapshotRestoreStateCode) -> str:
    return value


def from_ec2_query_text(text: str) -> FastSnapshotRestoreStateCode:
    return cast(FastSnapshotRestoreStateCode, text)


def serialize_ec2_query(
    value: FastSnapshotRestoreStateCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FastSnapshotRestoreStateCode:
    return from_ec2_query_text(el.text or "")
