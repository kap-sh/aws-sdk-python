"""Generated from Smithy shape ``com.amazonaws.rds#GlobalClusterMemberSynchronizationStatus``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

GlobalClusterMemberSynchronizationStatus: TypeAlias = Literal[
    "connected",
    "pending-resync",
]


# --- awsQuery ser/de ---
def to_query_text(value: GlobalClusterMemberSynchronizationStatus) -> str:
    return value


def from_query_text(text: str) -> GlobalClusterMemberSynchronizationStatus:
    return cast(GlobalClusterMemberSynchronizationStatus, text)


def serialize_query(
    value: GlobalClusterMemberSynchronizationStatus,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> GlobalClusterMemberSynchronizationStatus:
    return from_query_text(el.text or "")
