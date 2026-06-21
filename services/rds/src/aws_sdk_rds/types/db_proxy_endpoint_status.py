"""Generated from Smithy shape ``com.amazonaws.rds#DBProxyEndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

DBProxyEndpointStatus: TypeAlias = Literal[
    "available",
    "modifying",
    "incompatible-network",
    "insufficient-resource-limits",
    "creating",
    "deleting",
]


# --- awsQuery ser/de ---
def to_query_text(value: DBProxyEndpointStatus) -> str:
    return value


def from_query_text(text: str) -> DBProxyEndpointStatus:
    return cast(DBProxyEndpointStatus, text)


def serialize_query(
    value: DBProxyEndpointStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DBProxyEndpointStatus:
    return from_query_text(el.text or "")
