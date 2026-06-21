"""Generated from Smithy shape ``com.amazonaws.rds#DBProxyEndpointTargetRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

DBProxyEndpointTargetRole: TypeAlias = Literal[
    "READ_WRITE",
    "READ_ONLY",
]


# --- awsQuery ser/de ---
def to_query_text(value: DBProxyEndpointTargetRole) -> str:
    return value


def from_query_text(text: str) -> DBProxyEndpointTargetRole:
    return cast(DBProxyEndpointTargetRole, text)


def serialize_query(
    value: DBProxyEndpointTargetRole, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DBProxyEndpointTargetRole:
    return from_query_text(el.text or "")
