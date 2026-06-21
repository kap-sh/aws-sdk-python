"""Generated from Smithy shape ``com.amazonaws.rds#DBProxyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

DBProxyStatus: TypeAlias = Literal[
    "available",
    "modifying",
    "incompatible-network",
    "insufficient-resource-limits",
    "creating",
    "deleting",
    "suspended",
    "suspending",
    "reactivating",
]


# --- awsQuery ser/de ---
def to_query_text(value: DBProxyStatus) -> str:
    return value


def from_query_text(text: str) -> DBProxyStatus:
    return cast(DBProxyStatus, text)


def serialize_query(
    value: DBProxyStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DBProxyStatus:
    return from_query_text(el.text or "")
