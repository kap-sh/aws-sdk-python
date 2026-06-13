"""Generated from Smithy shape ``com.amazonaws.amp#CreateAnomalyDetectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.anomaly_detector_alias
    import aws_sdk_amp.types.anomaly_detector_configuration
    import aws_sdk_amp.types.anomaly_detector_evaluation_interval
    import aws_sdk_amp.types.anomaly_detector_missing_data_action
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.prometheus_metric_label_map
    import aws_sdk_amp.types.tag_map
    import aws_sdk_amp.types.workspace_id


class CreateAnomalyDetectorRequest(TypedDict):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace where the anomaly detector will be created.</p>"""
    alias: "aws_sdk_amp.types.anomaly_detector_alias.AnomalyDetectorAlias"
    """<p>A user-friendly name for the anomaly detector.</p>"""
    evaluation_interval_in_seconds: "aws_sdk_amp.types.anomaly_detector_evaluation_interval.AnomalyDetectorEvaluationInterval"
    """<p>The frequency, in seconds, at which the anomaly detector evaluates metrics. The default value is 60 seconds.</p>"""
    missing_data_action: NotRequired[
        "aws_sdk_amp.types.anomaly_detector_missing_data_action.AnomalyDetectorMissingDataAction"
    ]
    """<p>Specifies the action to take when data is missing during evaluation.</p>"""
    configuration: (
        "aws_sdk_amp.types.anomaly_detector_configuration.AnomalyDetectorConfiguration"
    )
    """<p>The algorithm configuration for the anomaly detector.</p>"""
    labels: NotRequired[
        "aws_sdk_amp.types.prometheus_metric_label_map.PrometheusMetricLabelMap"
    ]
    """<p>The Amazon Managed Service for Prometheus metric labels to associate with the anomaly detector.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["aws_sdk_amp.types.tag_map.TagMap"]
    """<p>The metadata to apply to the anomaly detector to assist with categorization and organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnomalyDetectorRequest) -> dict:
    out: dict = {}
    out["alias"] = value["alias"]
    out["evaluationIntervalInSeconds"] = value.get("evaluation_interval_in_seconds", 60)
    if "missing_data_action" in value:
        import aws_sdk_amp.types.anomaly_detector_missing_data_action

        out["missingDataAction"] = (
            aws_sdk_amp.types.anomaly_detector_missing_data_action.serialize_json(
                value["missing_data_action"]
            )
        )
    import aws_sdk_amp.types.anomaly_detector_configuration

    out["configuration"] = (
        aws_sdk_amp.types.anomaly_detector_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "labels" in value:
        import aws_sdk_amp.types.prometheus_metric_label_map

        out["labels"] = aws_sdk_amp.types.prometheus_metric_label_map.serialize_json(
            value["labels"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAnomalyDetectorRequest:
    out: CreateAnomalyDetectorRequest = {}  # type: ignore[typeddict-item]
    if "alias" in data:
        out["alias"] = data["alias"]
    else:
        raise DeserializationError("CreateAnomalyDetectorRequest.alias required")
    if "evaluationIntervalInSeconds" in data:
        out["evaluation_interval_in_seconds"] = data["evaluationIntervalInSeconds"]
    else:
        out["evaluation_interval_in_seconds"] = 60
    if "missingDataAction" in data:
        import aws_sdk_amp.types.anomaly_detector_missing_data_action

        out["missing_data_action"] = (
            aws_sdk_amp.types.anomaly_detector_missing_data_action.deserialize_json(
                data["missingDataAction"]
            )
        )
    if "configuration" in data:
        import aws_sdk_amp.types.anomaly_detector_configuration

        out["configuration"] = (
            aws_sdk_amp.types.anomaly_detector_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAnomalyDetectorRequest.configuration required"
        )
    if "labels" in data:
        import aws_sdk_amp.types.prometheus_metric_label_map

        out["labels"] = aws_sdk_amp.types.prometheus_metric_label_map.deserialize_json(
            data["labels"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.deserialize_json(data["tags"])
    return out
