"""Generated from Smithy shape ``com.amazonaws.eks#InsightResourceDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.insight_status
    import aws_sdk_eks.types.string


class InsightResourceDetail(TypedDict):
    insight_status: NotRequired["aws_sdk_eks.types.insight_status.InsightStatus"]
    """<p>An object containing more detail on the status of the insight resource.</p>"""
    kubernetes_resource_uri: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Kubernetes resource URI if applicable.</p>"""
    arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightResourceDetail) -> dict:
    out: dict = {}
    if "insight_status" in value:
        import aws_sdk_eks.types.insight_status

        out["insightStatus"] = aws_sdk_eks.types.insight_status.serialize_json(
            value["insight_status"]
        )
    if "kubernetes_resource_uri" in value:
        out["kubernetesResourceUri"] = value["kubernetes_resource_uri"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> InsightResourceDetail:
    out: InsightResourceDetail = {}  # type: ignore[typeddict-item]
    if "insightStatus" in data:
        import aws_sdk_eks.types.insight_status

        out["insight_status"] = aws_sdk_eks.types.insight_status.deserialize_json(
            data["insightStatus"]
        )
    if "kubernetesResourceUri" in data:
        out["kubernetes_resource_uri"] = data["kubernetesResourceUri"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
