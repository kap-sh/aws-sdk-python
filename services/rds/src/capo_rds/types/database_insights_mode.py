"""Generated from Smithy shape ``com.amazonaws.rds#DatabaseInsightsMode``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

DatabaseInsightsMode: TypeAlias = Literal[
    "standard",
    "advanced",
]


# --- awsQuery ser/de ---
def to_query_text(value: DatabaseInsightsMode) -> str:
    return value


def from_query_text(text: str) -> DatabaseInsightsMode:
    return cast(DatabaseInsightsMode, text)


def serialize_query(
    value: DatabaseInsightsMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DatabaseInsightsMode:
    return from_query_text(el.text or "")
