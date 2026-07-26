"""Generated from Smithy shape ``com.amazonaws.devopsguru#Recommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.recommendation_category
    import capo_devops_guru.types.recommendation_description
    import capo_devops_guru.types.recommendation_link
    import capo_devops_guru.types.recommendation_name
    import capo_devops_guru.types.recommendation_reason
    import capo_devops_guru.types.recommendation_related_anomalies
    import capo_devops_guru.types.recommendation_related_events


class Recommendation(TypedDict, closed=True):
    description: NotRequired[
        "capo_devops_guru.types.recommendation_description.RecommendationDescription"
    ]
    """<p> A description of the problem. </p>"""
    link: NotRequired["capo_devops_guru.types.recommendation_link.RecommendationLink"]
    """<p> A hyperlink to information to help you address the problem. </p>"""
    name: NotRequired["capo_devops_guru.types.recommendation_name.RecommendationName"]
    """<p> The name of the recommendation. </p>"""
    reason: NotRequired[
        "capo_devops_guru.types.recommendation_reason.RecommendationReason"
    ]
    """<p> The reason DevOps Guru flagged the anomalous behavior as a problem. </p>"""
    related_events: NotRequired[
        "capo_devops_guru.types.recommendation_related_events.RecommendationRelatedEvents"
    ]
    """<p> Events that are related to the problem. Use these events to learn more about what's happening and to help address the issue. </p>"""
    related_anomalies: NotRequired[
        "capo_devops_guru.types.recommendation_related_anomalies.RecommendationRelatedAnomalies"
    ]
    """<p> Anomalies that are related to the problem. Use these Anomalies to learn more about what's happening and to help address the issue. </p>"""
    category: NotRequired[
        "capo_devops_guru.types.recommendation_category.RecommendationCategory"
    ]
    """<p>The category type of the recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "link" in value:
        out["Link"] = value["link"]
    if "name" in value:
        out["Name"] = value["name"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "related_events" in value:
        import capo_devops_guru.types.recommendation_related_events

        out["RelatedEvents"] = (
            capo_devops_guru.types.recommendation_related_events.serialize_json(
                value["related_events"]
            )
        )
    if "related_anomalies" in value:
        import capo_devops_guru.types.recommendation_related_anomalies

        out["RelatedAnomalies"] = (
            capo_devops_guru.types.recommendation_related_anomalies.serialize_json(
                value["related_anomalies"]
            )
        )
    if "category" in value:
        out["Category"] = value["category"]
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Link" in data:
        out["link"] = data["Link"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    if "RelatedEvents" in data:
        import capo_devops_guru.types.recommendation_related_events

        out["related_events"] = (
            capo_devops_guru.types.recommendation_related_events.deserialize_json(
                data["RelatedEvents"]
            )
        )
    if "RelatedAnomalies" in data:
        import capo_devops_guru.types.recommendation_related_anomalies

        out["related_anomalies"] = (
            capo_devops_guru.types.recommendation_related_anomalies.deserialize_json(
                data["RelatedAnomalies"]
            )
        )
    if "Category" in data:
        out["category"] = data["Category"]
    return out
