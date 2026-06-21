"""Generated from Smithy shape ``com.amazonaws.rds#ReplicaMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

ReplicaMode: TypeAlias = Literal[
    "open-read-only",
    "mounted",
]


# --- awsQuery ser/de ---
def to_query_text(value: ReplicaMode) -> str:
    return value


def from_query_text(text: str) -> ReplicaMode:
    return cast(ReplicaMode, text)


def serialize_query(
    value: ReplicaMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReplicaMode:
    return from_query_text(el.text or "")
