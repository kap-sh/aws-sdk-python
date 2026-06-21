"""Generated from Smithy shape ``com.amazonaws.ec2#TieringOperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

TieringOperationStatus: TypeAlias = Literal[
    "archival-in-progress",
    "archival-completed",
    "archival-failed",
    "temporary-restore-in-progress",
    "temporary-restore-completed",
    "temporary-restore-failed",
    "permanent-restore-in-progress",
    "permanent-restore-completed",
    "permanent-restore-failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TieringOperationStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> TieringOperationStatus:
    return cast(TieringOperationStatus, text)


def serialize_ec2_query(
    value: TieringOperationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TieringOperationStatus:
    return from_ec2_query_text(el.text or "")
