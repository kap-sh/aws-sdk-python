"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServiceHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.analyzed_resource_count
    import aws_sdk_devops_guru.types.service_insight_health
    import aws_sdk_devops_guru.types.service_name


class ServiceHealth(TypedDict, closed=True):
    service_name: NotRequired["aws_sdk_devops_guru.types.service_name.ServiceName"]
    """<p>The name of the Amazon Web Services service.</p>"""
    insight: NotRequired[
        "aws_sdk_devops_guru.types.service_insight_health.ServiceInsightHealth"
    ]
    """<p>Represents the health of an Amazon Web Services service. This is a <code>ServiceInsightHealth</code> that contains the number of open proactive and reactive insights for this service.</p>"""
    analyzed_resource_count: NotRequired[
        "aws_sdk_devops_guru.types.analyzed_resource_count.AnalyzedResourceCount"
    ]
    """<p> Number of resources that DevOps Guru is monitoring in an analyzed Amazon Web Services service. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceHealth) -> dict:
    out: dict = {}
    if "service_name" in value:
        import aws_sdk_devops_guru.types.service_name

        out["ServiceName"] = aws_sdk_devops_guru.types.service_name.serialize_json(
            value["service_name"]
        )
    if "insight" in value:
        import aws_sdk_devops_guru.types.service_insight_health

        out["Insight"] = (
            aws_sdk_devops_guru.types.service_insight_health.serialize_json(
                value["insight"]
            )
        )
    if "analyzed_resource_count" in value:
        out["AnalyzedResourceCount"] = value["analyzed_resource_count"]
    return out


def deserialize_json(data: dict) -> ServiceHealth:
    out: ServiceHealth = {}  # type: ignore[typeddict-item]
    if "ServiceName" in data:
        import aws_sdk_devops_guru.types.service_name

        out["service_name"] = aws_sdk_devops_guru.types.service_name.deserialize_json(
            data["ServiceName"]
        )
    if "Insight" in data:
        import aws_sdk_devops_guru.types.service_insight_health

        out["insight"] = (
            aws_sdk_devops_guru.types.service_insight_health.deserialize_json(
                data["Insight"]
            )
        )
    if "AnalyzedResourceCount" in data:
        out["analyzed_resource_count"] = data["AnalyzedResourceCount"]
    return out
