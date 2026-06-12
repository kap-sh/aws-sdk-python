"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

NodeUpdateStatus: TypeAlias = Literal[
    "not-applied",
    "waiting-to-start",
    "in-progress",
    "stopping",
    "stopped",
    "complete",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "not-applied",
        "waiting-to-start",
        "in-progress",
        "stopping",
        "stopped",
        "complete",
    )
)


def to_query_text(value: NodeUpdateStatus) -> str:
    return value


def from_query_text(text: str) -> NodeUpdateStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown NodeUpdateStatus value: {text!r}")
    return cast(NodeUpdateStatus, text)


def serialize_query(
    value: NodeUpdateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> NodeUpdateStatus:
    return from_query_text(el.text or "")
