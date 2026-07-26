"""Generated from Smithy shape ``com.amazonaws.rds#DBRecommendationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_recommendation_list
    import capo_rds.types.string


class DBRecommendationsMessage(TypedDict, closed=True):
    db_recommendations: NotRequired[
        "capo_rds.types.db_recommendation_list.DBRecommendationList"
    ]
    """<p>A list of recommendations which is returned from <code>DescribeDBRecommendations</code> API request.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DBRecommendationsMessage</code> request. This token can be used later in a <code>DescribeDBRecomendations</code> request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBRecommendationsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_recommendations" in value:
        import capo_rds.types.db_recommendation_list

        capo_rds.types.db_recommendation_list.serialize_query(
            value["db_recommendations"], pairs, f"{prefix}.DBRecommendations"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DBRecommendationsMessage:
    out: DBRecommendationsMessage = {}  # type: ignore[typeddict-item]
    child_db_recommendations = el.find("DBRecommendations")
    if child_db_recommendations is not None:
        import capo_rds.types.db_recommendation_list

        out["db_recommendations"] = (
            capo_rds.types.db_recommendation_list.deserialize_query(
                child_db_recommendations
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
