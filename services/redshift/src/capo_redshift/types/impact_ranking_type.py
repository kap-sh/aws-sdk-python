"""Generated from Smithy shape ``com.amazonaws.redshift#ImpactRankingType``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

ImpactRankingType: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- awsQuery ser/de ---
def to_query_text(value: ImpactRankingType) -> str:
    return value


def from_query_text(text: str) -> ImpactRankingType:
    return cast(ImpactRankingType, text)


def serialize_query(
    value: ImpactRankingType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ImpactRankingType:
    return from_query_text(el.text or "")
