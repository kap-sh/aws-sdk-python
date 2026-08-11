"""Generated from Smithy shape ``com.amazonaws.rds#DBRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_recommendation

DBRecommendationList: TypeAlias = list[
    "capo_rds.types.db_recommendation.DBRecommendation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBRecommendationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_recommendation

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_recommendation.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> DBRecommendationList:
    import capo_rds.types.db_recommendation

    out: DBRecommendationList = []
    for child in el.findall("member"):
        out.append(capo_rds.types.db_recommendation.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBRecommendationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_recommendation

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_recommendation.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBRecommendationList:
    import capo_rds.types.db_recommendation

    out: DBRecommendationList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_recommendation.deserialize_query(child))
    return out
