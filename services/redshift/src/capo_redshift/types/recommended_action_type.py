"""Generated from Smithy shape ``com.amazonaws.redshift#RecommendedActionType``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

RecommendedActionType: TypeAlias = Literal[
    "SQL",
    "CLI",
]


# --- awsQuery ser/de ---
def to_query_text(value: RecommendedActionType) -> str:
    return value


def from_query_text(text: str) -> RecommendedActionType:
    return cast(RecommendedActionType, text)


def serialize_query(
    value: RecommendedActionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RecommendedActionType:
    return from_query_text(el.text or "")
