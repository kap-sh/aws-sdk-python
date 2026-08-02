"""Generated from Smithy shape ``com.amazonaws.rds#DBRecommendationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_recommendation


class DBRecommendationMessage(TypedDict, closed=True):
    db_recommendation: NotRequired["capo_rds.types.db_recommendation.DBRecommendation"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBRecommendationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_recommendation" in value:
        import capo_rds.types.db_recommendation

        capo_rds.types.db_recommendation.serialize_query(
            value["db_recommendation"], pairs, f"{key_prefix}DBRecommendation"
        )


def deserialize_query(el: Element) -> DBRecommendationMessage:
    out: DBRecommendationMessage = {}  # type: ignore[typeddict-item]
    child_db_recommendation = el.find("DBRecommendation")
    if child_db_recommendation is not None:
        import capo_rds.types.db_recommendation

        out["db_recommendation"] = capo_rds.types.db_recommendation.deserialize_query(
            child_db_recommendation
        )
    return out
