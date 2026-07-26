"""Generated from Smithy shape ``com.amazonaws.elasticache#ChangeType``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

ChangeType: TypeAlias = Literal[
    "immediate",
    "requires-reboot",
]


# --- awsQuery ser/de ---
def to_query_text(value: ChangeType) -> str:
    return value


def from_query_text(text: str) -> ChangeType:
    return cast(ChangeType, text)


def serialize_query(
    value: ChangeType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ChangeType:
    return from_query_text(el.text or "")
