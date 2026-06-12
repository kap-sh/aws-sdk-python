"""Generated from Smithy shape ``com.amazonaws.elasticache#ServiceUpdateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

ServiceUpdateType: TypeAlias = Literal["security-update",]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(("security-update",))


def to_query_text(value: ServiceUpdateType) -> str:
    return value


def from_query_text(text: str) -> ServiceUpdateType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ServiceUpdateType value: {text!r}")
    return cast(ServiceUpdateType, text)


def serialize_query(
    value: ServiceUpdateType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ServiceUpdateType:
    return from_query_text(el.text or "")
