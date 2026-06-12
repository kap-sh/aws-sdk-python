"""Generated from Smithy shape ``com.amazonaws.devopsguru#ReactiveInsightSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.associated_resource_arns
    import aws_sdk_devops_guru.types.insight_id
    import aws_sdk_devops_guru.types.insight_name
    import aws_sdk_devops_guru.types.insight_severity
    import aws_sdk_devops_guru.types.insight_status
    import aws_sdk_devops_guru.types.insight_time_range
    import aws_sdk_devops_guru.types.resource_collection
    import aws_sdk_devops_guru.types.service_collection


class ReactiveInsightSummary(TypedDict):
    id: NotRequired["aws_sdk_devops_guru.types.insight_id.InsightId"]
    """<p> The ID of a reactive summary. </p>"""
    name: NotRequired["aws_sdk_devops_guru.types.insight_name.InsightName"]
    """<p> The name of a reactive insight. </p>"""
    severity: NotRequired["aws_sdk_devops_guru.types.insight_severity.InsightSeverity"]
    """<p>The severity of the insight. For more information, see <a href=\"https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities\">Understanding insight severities</a> in the <i>Amazon DevOps Guru User Guide</i>.</p>"""
    status: NotRequired["aws_sdk_devops_guru.types.insight_status.InsightStatus"]
    """<p> The status of a reactive insight. </p>"""
    insight_time_range: NotRequired[
        "aws_sdk_devops_guru.types.insight_time_range.InsightTimeRange"
    ]
    resource_collection: NotRequired[
        "aws_sdk_devops_guru.types.resource_collection.ResourceCollection"
    ]
    service_collection: NotRequired[
        "aws_sdk_devops_guru.types.service_collection.ServiceCollection"
    ]
    """<p>A collection of the names of Amazon Web Services services.</p>"""
    associated_resource_arns: NotRequired[
        "aws_sdk_devops_guru.types.associated_resource_arns.AssociatedResourceArns"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Amazon Web Services resources that generated this insight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReactiveInsightSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "severity" in value:
        import aws_sdk_devops_guru.types.insight_severity

        out["Severity"] = aws_sdk_devops_guru.types.insight_severity.serialize_json(
            value["severity"]
        )
    if "status" in value:
        import aws_sdk_devops_guru.types.insight_status

        out["Status"] = aws_sdk_devops_guru.types.insight_status.serialize_json(
            value["status"]
        )
    if "insight_time_range" in value:
        import aws_sdk_devops_guru.types.insight_time_range

        out["InsightTimeRange"] = (
            aws_sdk_devops_guru.types.insight_time_range.serialize_json(
                value["insight_time_range"]
            )
        )
    if "resource_collection" in value:
        import aws_sdk_devops_guru.types.resource_collection

        out["ResourceCollection"] = (
            aws_sdk_devops_guru.types.resource_collection.serialize_json(
                value["resource_collection"]
            )
        )
    if "service_collection" in value:
        import aws_sdk_devops_guru.types.service_collection

        out["ServiceCollection"] = (
            aws_sdk_devops_guru.types.service_collection.serialize_json(
                value["service_collection"]
            )
        )
    if "associated_resource_arns" in value:
        import aws_sdk_devops_guru.types.associated_resource_arns

        out["AssociatedResourceArns"] = (
            aws_sdk_devops_guru.types.associated_resource_arns.serialize_json(
                value["associated_resource_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReactiveInsightSummary:
    out: ReactiveInsightSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Severity" in data:
        import aws_sdk_devops_guru.types.insight_severity

        out["severity"] = aws_sdk_devops_guru.types.insight_severity.deserialize_json(
            data["Severity"]
        )
    if "Status" in data:
        import aws_sdk_devops_guru.types.insight_status

        out["status"] = aws_sdk_devops_guru.types.insight_status.deserialize_json(
            data["Status"]
        )
    if "InsightTimeRange" in data:
        import aws_sdk_devops_guru.types.insight_time_range

        out["insight_time_range"] = (
            aws_sdk_devops_guru.types.insight_time_range.deserialize_json(
                data["InsightTimeRange"]
            )
        )
    if "ResourceCollection" in data:
        import aws_sdk_devops_guru.types.resource_collection

        out["resource_collection"] = (
            aws_sdk_devops_guru.types.resource_collection.deserialize_json(
                data["ResourceCollection"]
            )
        )
    if "ServiceCollection" in data:
        import aws_sdk_devops_guru.types.service_collection

        out["service_collection"] = (
            aws_sdk_devops_guru.types.service_collection.deserialize_json(
                data["ServiceCollection"]
            )
        )
    if "AssociatedResourceArns" in data:
        import aws_sdk_devops_guru.types.associated_resource_arns

        out["associated_resource_arns"] = (
            aws_sdk_devops_guru.types.associated_resource_arns.deserialize_json(
                data["AssociatedResourceArns"]
            )
        )
    return out
