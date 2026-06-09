"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerDataExportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

CapacityManagerDataExportStatus: TypeAlias = Literal[
    "pending",
    "in-progress",
    "delivered",
    "failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "in-progress",
        "delivered",
        "failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "in-progress",
        "delivered",
        "failed",
    )
)


def to_ec2_query_text(value: CapacityManagerDataExportStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityManagerDataExportStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityManagerDataExportStatus value: {text!r}"
        )
    return cast(CapacityManagerDataExportStatus, text)


def serialize_ec2_query(
    value: CapacityManagerDataExportStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityManagerDataExportStatus:
    return from_ec2_query_text(el.text or "")
