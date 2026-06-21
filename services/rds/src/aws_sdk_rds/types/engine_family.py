"""Generated from Smithy shape ``com.amazonaws.rds#EngineFamily``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

EngineFamily: TypeAlias = Literal[
    "MYSQL",
    "POSTGRESQL",
    "SQLSERVER",
]


# --- awsQuery ser/de ---
def to_query_text(value: EngineFamily) -> str:
    return value


def from_query_text(text: str) -> EngineFamily:
    return cast(EngineFamily, text)


def serialize_query(
    value: EngineFamily, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EngineFamily:
    return from_query_text(el.text or "")
