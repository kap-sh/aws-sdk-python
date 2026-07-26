"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotAttributeToSortBy``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

SnapshotAttributeToSortBy: TypeAlias = Literal[
    "SOURCE_TYPE",
    "TOTAL_SIZE",
    "CREATE_TIME",
]


# --- awsQuery ser/de ---
def to_query_text(value: SnapshotAttributeToSortBy) -> str:
    return value


def from_query_text(text: str) -> SnapshotAttributeToSortBy:
    return cast(SnapshotAttributeToSortBy, text)


def serialize_query(
    value: SnapshotAttributeToSortBy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SnapshotAttributeToSortBy:
    return from_query_text(el.text or "")
