"""Generated from Smithy shape ``com.amazonaws.elasticache#SlaMet``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

SlaMet: TypeAlias = Literal[
    "yes",
    "no",
    "n/a",
]


# --- awsQuery ser/de ---
def to_query_text(value: SlaMet) -> str:
    return value


def from_query_text(text: str) -> SlaMet:
    return cast(SlaMet, text)


def serialize_query(value: SlaMet, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SlaMet:
    return from_query_text(el.text or "")
