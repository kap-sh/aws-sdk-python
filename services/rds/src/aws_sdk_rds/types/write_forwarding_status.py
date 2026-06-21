"""Generated from Smithy shape ``com.amazonaws.rds#WriteForwardingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

WriteForwardingStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
    "enabling",
    "disabling",
    "unknown",
]


# --- awsQuery ser/de ---
def to_query_text(value: WriteForwardingStatus) -> str:
    return value


def from_query_text(text: str) -> WriteForwardingStatus:
    return cast(WriteForwardingStatus, text)


def serialize_query(
    value: WriteForwardingStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> WriteForwardingStatus:
    return from_query_text(el.text or "")
