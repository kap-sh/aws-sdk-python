"""Generated from Smithy shape ``com.amazonaws.redshift#SortByOrder``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

SortByOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- awsQuery ser/de ---
def to_query_text(value: SortByOrder) -> str:
    return value


def from_query_text(text: str) -> SortByOrder:
    return cast(SortByOrder, text)


def serialize_query(
    value: SortByOrder, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SortByOrder:
    return from_query_text(el.text or "")
