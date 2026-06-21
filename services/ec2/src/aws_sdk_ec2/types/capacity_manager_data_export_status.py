"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerDataExportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

CapacityManagerDataExportStatus: TypeAlias = Literal[
    "pending",
    "in-progress",
    "delivered",
    "failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CapacityManagerDataExportStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityManagerDataExportStatus:
    return cast(CapacityManagerDataExportStatus, text)


def serialize_ec2_query(
    value: CapacityManagerDataExportStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityManagerDataExportStatus:
    return from_ec2_query_text(el.text or "")
