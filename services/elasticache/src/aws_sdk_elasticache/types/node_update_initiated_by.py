"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeUpdateInitiatedBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

NodeUpdateInitiatedBy: TypeAlias = Literal[
    "system",
    "customer",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "system",
        "customer",
    )
)


def to_query_text(value: NodeUpdateInitiatedBy) -> str:
    return value


def from_query_text(text: str) -> NodeUpdateInitiatedBy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown NodeUpdateInitiatedBy value: {text!r}")
    return cast(NodeUpdateInitiatedBy, text)


def serialize_query(
    value: NodeUpdateInitiatedBy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> NodeUpdateInitiatedBy:
    return from_query_text(el.text or "")
