"""Generated from Smithy shape ``com.amazonaws.ec2#IngestionStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

IngestionStatus: TypeAlias = Literal[
    "initial-ingestion-in-progress",
    "ingestion-complete",
    "ingestion-failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IngestionStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> IngestionStatus:
    return cast(IngestionStatus, text)


def serialize_ec2_query(
    value: IngestionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IngestionStatus:
    return from_ec2_query_text(el.text or "")
