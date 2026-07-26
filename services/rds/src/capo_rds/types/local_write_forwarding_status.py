"""Generated from Smithy shape ``com.amazonaws.rds#LocalWriteForwardingStatus``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

LocalWriteForwardingStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
    "enabling",
    "disabling",
    "requested",
]


# --- awsQuery ser/de ---
def to_query_text(value: LocalWriteForwardingStatus) -> str:
    return value


def from_query_text(text: str) -> LocalWriteForwardingStatus:
    return cast(LocalWriteForwardingStatus, text)


def serialize_query(
    value: LocalWriteForwardingStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LocalWriteForwardingStatus:
    return from_query_text(el.text or "")
