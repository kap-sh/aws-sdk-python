"""Generated from Smithy shape ``com.amazonaws.elasticache#SourceType``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

SourceType: TypeAlias = Literal[
    "cache-cluster",
    "cache-parameter-group",
    "cache-security-group",
    "cache-subnet-group",
    "replication-group",
    "serverless-cache",
    "serverless-cache-snapshot",
    "user",
    "user-group",
]


# --- awsQuery ser/de ---
def to_query_text(value: SourceType) -> str:
    return value


def from_query_text(text: str) -> SourceType:
    return cast(SourceType, text)


def serialize_query(
    value: SourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SourceType:
    return from_query_text(el.text or "")
