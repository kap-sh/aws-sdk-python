"""Generated from Smithy shape ``com.amazonaws.devopsguru#ProactiveAnomalySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.anomaly_description
    import aws_sdk_devops_guru.types.anomaly_id
    import aws_sdk_devops_guru.types.anomaly_limit
    import aws_sdk_devops_guru.types.anomaly_reported_time_range
    import aws_sdk_devops_guru.types.anomaly_resources
    import aws_sdk_devops_guru.types.anomaly_severity
    import aws_sdk_devops_guru.types.anomaly_source_details
    import aws_sdk_devops_guru.types.anomaly_source_metadata
    import aws_sdk_devops_guru.types.anomaly_status
    import aws_sdk_devops_guru.types.anomaly_time_range
    import aws_sdk_devops_guru.types.insight_id
    import aws_sdk_devops_guru.types.prediction_time_range
    import aws_sdk_devops_guru.types.resource_collection
    import aws_sdk_devops_guru.types.timestamp


class ProactiveAnomalySummary(TypedDict):
    id: NotRequired["aws_sdk_devops_guru.types.anomaly_id.AnomalyId"]
    """<p>The ID of the anomaly.</p>"""
    severity: NotRequired["aws_sdk_devops_guru.types.anomaly_severity.AnomalySeverity"]
    r"""<p>The severity of the anomaly. The severity of anomalies that generate an insight determine that insight's severity. For more information, see <a href=\"https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities\">Understanding insight severities</a> in the <i>Amazon DevOps Guru User Guide</i>.</p>"""
    status: NotRequired["aws_sdk_devops_guru.types.anomaly_status.AnomalyStatus"]
    """<p>The status of the anomaly.</p>"""
    update_time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> The time of the anomaly's most recent update. </p>"""
    anomaly_time_range: NotRequired[
        "aws_sdk_devops_guru.types.anomaly_time_range.AnomalyTimeRange"
    ]
    anomaly_reported_time_range: NotRequired[
        "aws_sdk_devops_guru.types.anomaly_reported_time_range.AnomalyReportedTimeRange"
    ]
    """<p> An <code>AnomalyReportedTimeRange</code> object that specifies the time range between when the anomaly is opened and the time when it is closed. </p>"""
    prediction_time_range: NotRequired[
        "aws_sdk_devops_guru.types.prediction_time_range.PredictionTimeRange"
    ]
    source_details: NotRequired[
        "aws_sdk_devops_guru.types.anomaly_source_details.AnomalySourceDetails"
    ]
    """<p> Details about the source of the analyzed operational data that triggered the anomaly. The one supported source is Amazon CloudWatch metrics. </p>"""
    associated_insight_id: NotRequired["aws_sdk_devops_guru.types.insight_id.InsightId"]
    """<p> The ID of the insight that contains this anomaly. An insight is composed of related anomalies. </p>"""
    resource_collection: NotRequired[
        "aws_sdk_devops_guru.types.resource_collection.ResourceCollection"
    ]
    limit: NotRequired["aws_sdk_devops_guru.types.anomaly_limit.AnomalyLimit"]
    """<p> A threshold that was exceeded by behavior in analyzed resources. Exceeding this threshold is related to the anomalous behavior that generated this anomaly. </p>"""
    source_metadata: NotRequired[
        "aws_sdk_devops_guru.types.anomaly_source_metadata.AnomalySourceMetadata"
    ]
    """<p>The metadata of the source which detects proactive anomalies.</p>"""
    anomaly_resources: NotRequired[
        "aws_sdk_devops_guru.types.anomaly_resources.AnomalyResources"
    ]
    """<p>Information about a resource in which DevOps Guru detected anomalous behavior.</p>"""
    description: NotRequired[
        "aws_sdk_devops_guru.types.anomaly_description.AnomalyDescription"
    ]
    """<p> A description of the proactive anomaly. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProactiveAnomalySummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "severity" in value:
        import aws_sdk_devops_guru.types.anomaly_severity

        out["Severity"] = aws_sdk_devops_guru.types.anomaly_severity.serialize_json(
            value["severity"]
        )
    if "status" in value:
        import aws_sdk_devops_guru.types.anomaly_status

        out["Status"] = aws_sdk_devops_guru.types.anomaly_status.serialize_json(
            value["status"]
        )
    if "update_time" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["UpdateTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["update_time"]
        )
    if "anomaly_time_range" in value:
        import aws_sdk_devops_guru.types.anomaly_time_range

        out["AnomalyTimeRange"] = (
            aws_sdk_devops_guru.types.anomaly_time_range.serialize_json(
                value["anomaly_time_range"]
            )
        )
    if "anomaly_reported_time_range" in value:
        import aws_sdk_devops_guru.types.anomaly_reported_time_range

        out["AnomalyReportedTimeRange"] = (
            aws_sdk_devops_guru.types.anomaly_reported_time_range.serialize_json(
                value["anomaly_reported_time_range"]
            )
        )
    if "prediction_time_range" in value:
        import aws_sdk_devops_guru.types.prediction_time_range

        out["PredictionTimeRange"] = (
            aws_sdk_devops_guru.types.prediction_time_range.serialize_json(
                value["prediction_time_range"]
            )
        )
    if "source_details" in value:
        import aws_sdk_devops_guru.types.anomaly_source_details

        out["SourceDetails"] = (
            aws_sdk_devops_guru.types.anomaly_source_details.serialize_json(
                value["source_details"]
            )
        )
    if "associated_insight_id" in value:
        out["AssociatedInsightId"] = value["associated_insight_id"]
    if "resource_collection" in value:
        import aws_sdk_devops_guru.types.resource_collection

        out["ResourceCollection"] = (
            aws_sdk_devops_guru.types.resource_collection.serialize_json(
                value["resource_collection"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "source_metadata" in value:
        import aws_sdk_devops_guru.types.anomaly_source_metadata

        out["SourceMetadata"] = (
            aws_sdk_devops_guru.types.anomaly_source_metadata.serialize_json(
                value["source_metadata"]
            )
        )
    if "anomaly_resources" in value:
        import aws_sdk_devops_guru.types.anomaly_resources

        out["AnomalyResources"] = (
            aws_sdk_devops_guru.types.anomaly_resources.serialize_json(
                value["anomaly_resources"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ProactiveAnomalySummary:
    out: ProactiveAnomalySummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Severity" in data:
        import aws_sdk_devops_guru.types.anomaly_severity

        out["severity"] = aws_sdk_devops_guru.types.anomaly_severity.deserialize_json(
            data["Severity"]
        )
    if "Status" in data:
        import aws_sdk_devops_guru.types.anomaly_status

        out["status"] = aws_sdk_devops_guru.types.anomaly_status.deserialize_json(
            data["Status"]
        )
    if "UpdateTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["update_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    if "AnomalyTimeRange" in data:
        import aws_sdk_devops_guru.types.anomaly_time_range

        out["anomaly_time_range"] = (
            aws_sdk_devops_guru.types.anomaly_time_range.deserialize_json(
                data["AnomalyTimeRange"]
            )
        )
    if "AnomalyReportedTimeRange" in data:
        import aws_sdk_devops_guru.types.anomaly_reported_time_range

        out["anomaly_reported_time_range"] = (
            aws_sdk_devops_guru.types.anomaly_reported_time_range.deserialize_json(
                data["AnomalyReportedTimeRange"]
            )
        )
    if "PredictionTimeRange" in data:
        import aws_sdk_devops_guru.types.prediction_time_range

        out["prediction_time_range"] = (
            aws_sdk_devops_guru.types.prediction_time_range.deserialize_json(
                data["PredictionTimeRange"]
            )
        )
    if "SourceDetails" in data:
        import aws_sdk_devops_guru.types.anomaly_source_details

        out["source_details"] = (
            aws_sdk_devops_guru.types.anomaly_source_details.deserialize_json(
                data["SourceDetails"]
            )
        )
    if "AssociatedInsightId" in data:
        out["associated_insight_id"] = data["AssociatedInsightId"]
    if "ResourceCollection" in data:
        import aws_sdk_devops_guru.types.resource_collection

        out["resource_collection"] = (
            aws_sdk_devops_guru.types.resource_collection.deserialize_json(
                data["ResourceCollection"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "SourceMetadata" in data:
        import aws_sdk_devops_guru.types.anomaly_source_metadata

        out["source_metadata"] = (
            aws_sdk_devops_guru.types.anomaly_source_metadata.deserialize_json(
                data["SourceMetadata"]
            )
        )
    if "AnomalyResources" in data:
        import aws_sdk_devops_guru.types.anomaly_resources

        out["anomaly_resources"] = (
            aws_sdk_devops_guru.types.anomaly_resources.deserialize_json(
                data["AnomalyResources"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
