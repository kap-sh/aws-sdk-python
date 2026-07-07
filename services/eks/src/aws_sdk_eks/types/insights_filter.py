"""Generated from Smithy shape ``com.amazonaws.eks#InsightsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.category_list
    import aws_sdk_eks.types.insight_status_value_list
    import aws_sdk_eks.types.string_list


class InsightsFilter(TypedDict, closed=True):
    categories: NotRequired["aws_sdk_eks.types.category_list.CategoryList"]
    """<p>The categories to use to filter insights. The following lists the available categories:</p> <ul> <li> <p> <code>UPGRADE_READINESS</code>: Amazon EKS identifies issues that could impact your ability to upgrade to new versions of Kubernetes. These are called upgrade insights.</p> </li> <li> <p> <code>MISCONFIGURATION</code>: Amazon EKS identifies misconfiguration in your EKS Hybrid Nodes setup that could impair functionality of your cluster or workloads. These are called configuration insights.</p> </li> </ul>"""
    kubernetes_versions: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The Kubernetes versions to use to filter the insights.</p>"""
    statuses: NotRequired[
        "aws_sdk_eks.types.insight_status_value_list.InsightStatusValueList"
    ]
    """<p>The statuses to use to filter the insights. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightsFilter) -> dict:
    out: dict = {}
    if "categories" in value:
        import aws_sdk_eks.types.category_list

        out["categories"] = aws_sdk_eks.types.category_list.serialize_json(
            value["categories"]
        )
    if "kubernetes_versions" in value:
        import aws_sdk_eks.types.string_list

        out["kubernetesVersions"] = aws_sdk_eks.types.string_list.serialize_json(
            value["kubernetes_versions"]
        )
    if "statuses" in value:
        import aws_sdk_eks.types.insight_status_value_list

        out["statuses"] = aws_sdk_eks.types.insight_status_value_list.serialize_json(
            value["statuses"]
        )
    return out


def deserialize_json(data: dict) -> InsightsFilter:
    out: InsightsFilter = {}  # type: ignore[typeddict-item]
    if "categories" in data:
        import aws_sdk_eks.types.category_list

        out["categories"] = aws_sdk_eks.types.category_list.deserialize_json(
            data["categories"]
        )
    if "kubernetesVersions" in data:
        import aws_sdk_eks.types.string_list

        out["kubernetes_versions"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["kubernetesVersions"]
        )
    if "statuses" in data:
        import aws_sdk_eks.types.insight_status_value_list

        out["statuses"] = aws_sdk_eks.types.insight_status_value_list.deserialize_json(
            data["statuses"]
        )
    return out
