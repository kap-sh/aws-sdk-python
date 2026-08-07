"""Generated from Smithy shape ``com.amazonaws.redshift#ListRecommendationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.recommendation_list
    import capo_redshift.types.string


class ListRecommendationsResult(TypedDict, closed=True):
    recommendations: NotRequired[
        "capo_redshift.types.recommendation_list.RecommendationList"
    ]
    """<p>The Advisor recommendations for action on the Amazon Redshift cluster.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListRecommendationsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "recommendations" in value:
        import capo_redshift.types.recommendation_list

        capo_redshift.types.recommendation_list.serialize_query(
            value["recommendations"], pairs, f"{key_prefix}Recommendations"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> ListRecommendationsResult:
    out: ListRecommendationsResult = {}  # type: ignore[typeddict-item]
    child_recommendations = el.find("Recommendations")
    if child_recommendations is not None:
        import capo_redshift.types.recommendation_list

        out["recommendations"] = (
            capo_redshift.types.recommendation_list.deserialize_query(
                child_recommendations
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
