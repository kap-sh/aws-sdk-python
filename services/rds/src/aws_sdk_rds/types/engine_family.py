"""Generated from Smithy shape ``com.amazonaws.rds#EngineFamily``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

EngineFamily: TypeAlias = Literal[
    "MYSQL",
    "POSTGRESQL",
    "SQLSERVER",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MYSQL",
        "POSTGRESQL",
        "SQLSERVER",
    )
)


def to_query_text(value: EngineFamily) -> str:
    return value


def from_query_text(text: str) -> EngineFamily:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EngineFamily value: {text!r}")
    return cast(EngineFamily, text)


def serialize_query(
    value: EngineFamily, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EngineFamily:
    return from_query_text(el.text or "")
