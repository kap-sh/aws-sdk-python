"""Generated from Smithy shape ``com.amazonaws.eks#InsightSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.category
    import aws_sdk_eks.types.insight_status
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.timestamp


class InsightSummary(TypedDict):
    id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The ID of the insight.</p>"""
    name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the insight.</p>"""
    category: NotRequired["aws_sdk_eks.types.category.Category"]
    """<p>The category of the insight.</p>"""
    kubernetes_version: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Kubernetes minor version associated with an insight if applicable. </p>"""
    last_refresh_time: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The time Amazon EKS last successfully completed a refresh of this insight check on the cluster.</p>"""
    last_transition_time: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The time the status of the insight last changed.</p>"""
    description: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The description of the insight which includes alert criteria, remediation recommendation, and additional resources (contains Markdown).</p>"""
    insight_status: NotRequired["aws_sdk_eks.types.insight_status.InsightStatus"]
    """<p>An object containing more detail on the status of the insight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "category" in value:
        import aws_sdk_eks.types.category

        out["category"] = aws_sdk_eks.types.category.serialize_json(value["category"])
    if "kubernetes_version" in value:
        out["kubernetesVersion"] = value["kubernetes_version"]
    if "last_refresh_time" in value:
        import aws_sdk_eks.types.timestamp

        out["lastRefreshTime"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["last_refresh_time"]
        )
    if "last_transition_time" in value:
        import aws_sdk_eks.types.timestamp

        out["lastTransitionTime"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["last_transition_time"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "insight_status" in value:
        import aws_sdk_eks.types.insight_status

        out["insightStatus"] = aws_sdk_eks.types.insight_status.serialize_json(
            value["insight_status"]
        )
    return out


def deserialize_json(data: dict) -> InsightSummary:
    out: InsightSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "category" in data:
        import aws_sdk_eks.types.category

        out["category"] = aws_sdk_eks.types.category.deserialize_json(data["category"])
    if "kubernetesVersion" in data:
        out["kubernetes_version"] = data["kubernetesVersion"]
    if "lastRefreshTime" in data:
        import aws_sdk_eks.types.timestamp

        out["last_refresh_time"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["lastRefreshTime"]
        )
    if "lastTransitionTime" in data:
        import aws_sdk_eks.types.timestamp

        out["last_transition_time"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["lastTransitionTime"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "insightStatus" in data:
        import aws_sdk_eks.types.insight_status

        out["insight_status"] = aws_sdk_eks.types.insight_status.deserialize_json(
            data["insightStatus"]
        )
    return out
