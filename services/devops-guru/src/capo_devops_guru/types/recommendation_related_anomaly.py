"""Generated from Smithy shape ``com.amazonaws.devopsguru#RecommendationRelatedAnomaly``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.anomaly_id
    import capo_devops_guru.types.recommendation_related_anomaly_resources
    import capo_devops_guru.types.related_anomaly_source_details


class RecommendationRelatedAnomaly(TypedDict, closed=True):
    resources: NotRequired[
        "capo_devops_guru.types.recommendation_related_anomaly_resources.RecommendationRelatedAnomalyResources"
    ]
    """<p> An array of objects that represent resources in which DevOps Guru detected anomalous behavior. Each object contains the name and type of the resource. </p>"""
    source_details: NotRequired[
        "capo_devops_guru.types.related_anomaly_source_details.RelatedAnomalySourceDetails"
    ]
    """<p> Information about where the anomalous behavior related the recommendation was found. For example, details in Amazon CloudWatch metrics. </p>"""
    anomaly_id: NotRequired["capo_devops_guru.types.anomaly_id.AnomalyId"]
    """<p>The ID of an anomaly that generated the insight with this recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationRelatedAnomaly) -> dict:
    out: dict = {}
    if "resources" in value:
        import capo_devops_guru.types.recommendation_related_anomaly_resources

        out["Resources"] = (
            capo_devops_guru.types.recommendation_related_anomaly_resources.serialize_json(
                value["resources"]
            )
        )
    if "source_details" in value:
        import capo_devops_guru.types.related_anomaly_source_details

        out["SourceDetails"] = (
            capo_devops_guru.types.related_anomaly_source_details.serialize_json(
                value["source_details"]
            )
        )
    if "anomaly_id" in value:
        out["AnomalyId"] = value["anomaly_id"]
    return out


def deserialize_json(data: dict) -> RecommendationRelatedAnomaly:
    out: RecommendationRelatedAnomaly = {}  # type: ignore[typeddict-item]
    if "Resources" in data:
        import capo_devops_guru.types.recommendation_related_anomaly_resources

        out["resources"] = (
            capo_devops_guru.types.recommendation_related_anomaly_resources.deserialize_json(
                data["Resources"]
            )
        )
    if "SourceDetails" in data:
        import capo_devops_guru.types.related_anomaly_source_details

        out["source_details"] = (
            capo_devops_guru.types.related_anomaly_source_details.deserialize_json(
                data["SourceDetails"]
            )
        )
    if "AnomalyId" in data:
        out["anomaly_id"] = data["AnomalyId"]
    return out
