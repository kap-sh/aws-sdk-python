"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotReturnCodes``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

SnapshotReturnCodes: TypeAlias = Literal[
    "success",
    "skipped",
    "missing-permissions",
    "internal-error",
    "client-error",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "success",
        "skipped",
        "missing-permissions",
        "internal-error",
        "client-error",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "success",
        "skipped",
        "missing-permissions",
        "internal-error",
        "client-error",
    )
)


def to_ec2_query_text(value: SnapshotReturnCodes) -> str:
    return value


def from_ec2_query_text(text: str) -> SnapshotReturnCodes:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SnapshotReturnCodes value: {text!r}")
    return cast(SnapshotReturnCodes, text)


def serialize_ec2_query(
    value: SnapshotReturnCodes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SnapshotReturnCodes:
    return from_ec2_query_text(el.text or "")
