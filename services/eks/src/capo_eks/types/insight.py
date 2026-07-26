"""Generated from Smithy shape ``com.amazonaws.eks#Insight``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.additional_info_map
    import capo_eks.types.category
    import capo_eks.types.insight_category_specific_summary
    import capo_eks.types.insight_resource_details
    import capo_eks.types.insight_status
    import capo_eks.types.string
    import capo_eks.types.timestamp


class Insight(TypedDict, closed=True):
    id: NotRequired["capo_eks.types.string.String"]
    """<p>The ID of the insight.</p>"""
    name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the insight.</p>"""
    category: NotRequired["capo_eks.types.category.Category"]
    """<p>The category of the insight.</p>"""
    kubernetes_version: NotRequired["capo_eks.types.string.String"]
    """<p>The Kubernetes minor version associated with an insight if applicable.</p>"""
    last_refresh_time: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The time Amazon EKS last successfully completed a refresh of this insight check on the cluster.</p>"""
    last_transition_time: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The time the status of the insight last changed.</p>"""
    description: NotRequired["capo_eks.types.string.String"]
    """<p>The description of the insight which includes alert criteria, remediation recommendation, and additional resources (contains Markdown).</p>"""
    insight_status: NotRequired["capo_eks.types.insight_status.InsightStatus"]
    """<p>An object containing more detail on the status of the insight resource.</p>"""
    recommendation: NotRequired["capo_eks.types.string.String"]
    """<p>A summary of how to remediate the finding of this insight if applicable. </p>"""
    additional_info: NotRequired["capo_eks.types.additional_info_map.AdditionalInfoMap"]
    """<p>Links to sources that provide additional context on the insight.</p>"""
    resources: NotRequired[
        "capo_eks.types.insight_resource_details.InsightResourceDetails"
    ]
    """<p>The details about each resource listed in the insight check result.</p>"""
    category_specific_summary: NotRequired[
        "capo_eks.types.insight_category_specific_summary.InsightCategorySpecificSummary"
    ]
    """<p>Summary information that relates to the category of the insight. Currently only returned with certain insights having category <code>UPGRADE_READINESS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Insight) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "category" in value:
        import capo_eks.types.category

        out["category"] = capo_eks.types.category.serialize_json(value["category"])
    if "kubernetes_version" in value:
        out["kubernetesVersion"] = value["kubernetes_version"]
    if "last_refresh_time" in value:
        import capo_eks.types.timestamp

        out["lastRefreshTime"] = capo_eks.types.timestamp.serialize_json(
            value["last_refresh_time"]
        )
    if "last_transition_time" in value:
        import capo_eks.types.timestamp

        out["lastTransitionTime"] = capo_eks.types.timestamp.serialize_json(
            value["last_transition_time"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "insight_status" in value:
        import capo_eks.types.insight_status

        out["insightStatus"] = capo_eks.types.insight_status.serialize_json(
            value["insight_status"]
        )
    if "recommendation" in value:
        out["recommendation"] = value["recommendation"]
    if "additional_info" in value:
        import capo_eks.types.additional_info_map

        out["additionalInfo"] = capo_eks.types.additional_info_map.serialize_json(
            value["additional_info"]
        )
    if "resources" in value:
        import capo_eks.types.insight_resource_details

        out["resources"] = capo_eks.types.insight_resource_details.serialize_json(
            value["resources"]
        )
    if "category_specific_summary" in value:
        import capo_eks.types.insight_category_specific_summary

        out["categorySpecificSummary"] = (
            capo_eks.types.insight_category_specific_summary.serialize_json(
                value["category_specific_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> Insight:
    out: Insight = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "category" in data:
        import capo_eks.types.category

        out["category"] = capo_eks.types.category.deserialize_json(data["category"])
    if "kubernetesVersion" in data:
        out["kubernetes_version"] = data["kubernetesVersion"]
    if "lastRefreshTime" in data:
        import capo_eks.types.timestamp

        out["last_refresh_time"] = capo_eks.types.timestamp.deserialize_json(
            data["lastRefreshTime"]
        )
    if "lastTransitionTime" in data:
        import capo_eks.types.timestamp

        out["last_transition_time"] = capo_eks.types.timestamp.deserialize_json(
            data["lastTransitionTime"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "insightStatus" in data:
        import capo_eks.types.insight_status

        out["insight_status"] = capo_eks.types.insight_status.deserialize_json(
            data["insightStatus"]
        )
    if "recommendation" in data:
        out["recommendation"] = data["recommendation"]
    if "additionalInfo" in data:
        import capo_eks.types.additional_info_map

        out["additional_info"] = capo_eks.types.additional_info_map.deserialize_json(
            data["additionalInfo"]
        )
    if "resources" in data:
        import capo_eks.types.insight_resource_details

        out["resources"] = capo_eks.types.insight_resource_details.deserialize_json(
            data["resources"]
        )
    if "categorySpecificSummary" in data:
        import capo_eks.types.insight_category_specific_summary

        out["category_specific_summary"] = (
            capo_eks.types.insight_category_specific_summary.deserialize_json(
                data["categorySpecificSummary"]
            )
        )
    return out
