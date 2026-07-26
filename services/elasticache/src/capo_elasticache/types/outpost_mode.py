"""Generated from Smithy shape ``com.amazonaws.elasticache#OutpostMode``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

OutpostMode: TypeAlias = Literal[
    "single-outpost",
    "cross-outpost",
]


# --- awsQuery ser/de ---
def to_query_text(value: OutpostMode) -> str:
    return value


def from_query_text(text: str) -> OutpostMode:
    return cast(OutpostMode, text)


def serialize_query(
    value: OutpostMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OutpostMode:
    return from_query_text(el.text or "")
