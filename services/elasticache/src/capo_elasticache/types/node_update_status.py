"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

NodeUpdateStatus: TypeAlias = Literal[
    "not-applied",
    "waiting-to-start",
    "in-progress",
    "stopping",
    "stopped",
    "complete",
]


# --- awsQuery ser/de ---
def to_query_text(value: NodeUpdateStatus) -> str:
    return value


def from_query_text(text: str) -> NodeUpdateStatus:
    return cast(NodeUpdateStatus, text)


def serialize_query(
    value: NodeUpdateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> NodeUpdateStatus:
    return from_query_text(el.text or "")
