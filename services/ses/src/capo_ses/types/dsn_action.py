"""Generated from Smithy shape ``com.amazonaws.ses#DsnAction``."""

from typing import Literal, TypeAlias, cast

from capo_ses._protocol.xml import Element

DsnAction: TypeAlias = Literal[
    "failed",
    "delayed",
    "delivered",
    "relayed",
    "expanded",
]


# --- awsQuery ser/de ---
def to_query_text(value: DsnAction) -> str:
    return value


def from_query_text(text: str) -> DsnAction:
    return cast(DsnAction, text)


def serialize_query(
    value: DsnAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DsnAction:
    return from_query_text(el.text or "")
