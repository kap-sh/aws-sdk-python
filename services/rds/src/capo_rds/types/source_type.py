"""Generated from Smithy shape ``com.amazonaws.rds#SourceType``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

SourceType: TypeAlias = Literal[
    "db-instance",
    "db-parameter-group",
    "db-security-group",
    "db-snapshot",
    "db-cluster",
    "db-cluster-snapshot",
    "custom-engine-version",
    "db-proxy",
    "blue-green-deployment",
    "db-shard-group",
    "zero-etl",
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
