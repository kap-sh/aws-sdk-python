"""Generated from Smithy shape ``com.amazonaws.redshift#RecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.recommendation

RecommendationList: TypeAlias = list[
    "capo_redshift.types.recommendation.Recommendation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RecommendationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.recommendation

    for n, item in enumerate(value, 1):
        capo_redshift.types.recommendation.serialize_query(
            item, pairs, f"{prefix}.Recommendation.{n}"
        )


def deserialize_query(el: Element) -> RecommendationList:
    import capo_redshift.types.recommendation

    out: RecommendationList = []
    for child in el.findall("Recommendation"):
        out.append(capo_redshift.types.recommendation.deserialize_query(child))
    return out


def serialize_query_flat(
    value: RecommendationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.recommendation

    for n, item in enumerate(value, 1):
        capo_redshift.types.recommendation.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> RecommendationList:
    import capo_redshift.types.recommendation

    out: RecommendationList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.recommendation.deserialize_query(child))
    return out
