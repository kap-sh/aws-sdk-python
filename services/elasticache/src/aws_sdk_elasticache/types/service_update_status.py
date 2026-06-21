"""Generated from Smithy shape ``com.amazonaws.elasticache#ServiceUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element

ServiceUpdateStatus: TypeAlias = Literal[
    "available",
    "cancelled",
    "expired",
]


# --- awsQuery ser/de ---
def to_query_text(value: ServiceUpdateStatus) -> str:
    return value


def from_query_text(text: str) -> ServiceUpdateStatus:
    return cast(ServiceUpdateStatus, text)


def serialize_query(
    value: ServiceUpdateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ServiceUpdateStatus:
    return from_query_text(el.text or "")
