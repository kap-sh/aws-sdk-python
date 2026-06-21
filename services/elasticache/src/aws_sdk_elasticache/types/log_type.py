"""Generated from Smithy shape ``com.amazonaws.elasticache#LogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element

LogType: TypeAlias = Literal[
    "slow-log",
    "engine-log",
]


# --- awsQuery ser/de ---
def to_query_text(value: LogType) -> str:
    return value


def from_query_text(text: str) -> LogType:
    return cast(LogType, text)


def serialize_query(value: LogType, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LogType:
    return from_query_text(el.text or "")
