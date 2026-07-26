"""Generated from Smithy shape ``com.amazonaws.amp#AnomalyDetectorDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_amp.types.anomaly_detector_alias
    import capo_amp.types.anomaly_detector_arn
    import capo_amp.types.anomaly_detector_configuration
    import capo_amp.types.anomaly_detector_evaluation_interval
    import capo_amp.types.anomaly_detector_id
    import capo_amp.types.anomaly_detector_missing_data_action
    import capo_amp.types.anomaly_detector_status
    import capo_amp.types.prometheus_metric_label_map
    import capo_amp.types.tag_map


class AnomalyDetectorDescription(TypedDict, closed=True):
    arn: "capo_amp.types.anomaly_detector_arn.AnomalyDetectorArn"
    """<p>The Amazon Resource Name (ARN) of the anomaly detector.</p>"""
    anomaly_detector_id: "capo_amp.types.anomaly_detector_id.AnomalyDetectorId"
    """<p>The unique identifier of the anomaly detector.</p>"""
    alias: "capo_amp.types.anomaly_detector_alias.AnomalyDetectorAlias"
    """<p>The user-friendly name of the anomaly detector.</p>"""
    evaluation_interval_in_seconds: NotRequired[
        "capo_amp.types.anomaly_detector_evaluation_interval.AnomalyDetectorEvaluationInterval"
    ]
    """<p>The frequency, in seconds, at which the anomaly detector evaluates metrics.</p>"""
    missing_data_action: NotRequired[
        "capo_amp.types.anomaly_detector_missing_data_action.AnomalyDetectorMissingDataAction"
    ]
    """<p>The action taken when data is missing during evaluation.</p>"""
    configuration: NotRequired[
        "capo_amp.types.anomaly_detector_configuration.AnomalyDetectorConfiguration"
    ]
    """<p>The algorithm configuration of the anomaly detector.</p>"""
    labels: NotRequired[
        "capo_amp.types.prometheus_metric_label_map.PrometheusMetricLabelMap"
    ]
    """<p>The Amazon Managed Service for Prometheus metric labels associated with the anomaly detector.</p>"""
    status: "capo_amp.types.anomaly_detector_status.AnomalyDetectorStatus"
    """<p>The current status of the anomaly detector.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the anomaly detector was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The timestamp when the anomaly detector was last modified.</p>"""
    tags: NotRequired["capo_amp.types.tag_map.TagMap"]
    """<p>The tags applied to the anomaly detector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyDetectorDescription) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["anomalyDetectorId"] = value["anomaly_detector_id"]
    out["alias"] = value["alias"]
    if "evaluation_interval_in_seconds" in value:
        out["evaluationIntervalInSeconds"] = value["evaluation_interval_in_seconds"]
    if "missing_data_action" in value:
        import capo_amp.types.anomaly_detector_missing_data_action

        out["missingDataAction"] = (
            capo_amp.types.anomaly_detector_missing_data_action.serialize_json(
                value["missing_data_action"]
            )
        )
    if "configuration" in value:
        import capo_amp.types.anomaly_detector_configuration

        out["configuration"] = (
            capo_amp.types.anomaly_detector_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "labels" in value:
        import capo_amp.types.prometheus_metric_label_map

        out["labels"] = capo_amp.types.prometheus_metric_label_map.serialize_json(
            value["labels"]
        )
    import capo_amp.types.anomaly_detector_status

    out["status"] = capo_amp.types.anomaly_detector_status.serialize_json(
        value["status"]
    )
    import capo_amp.types._prelude.timestamp

    out["createdAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_amp.types._prelude.timestamp

    out["modifiedAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    if "tags" in value:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AnomalyDetectorDescription:
    out: AnomalyDetectorDescription = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AnomalyDetectorDescription.arn required")
    if "anomalyDetectorId" in data:
        out["anomaly_detector_id"] = data["anomalyDetectorId"]
    else:
        raise DeserializationError(
            "AnomalyDetectorDescription.anomaly_detector_id required"
        )
    if "alias" in data:
        out["alias"] = data["alias"]
    else:
        raise DeserializationError("AnomalyDetectorDescription.alias required")
    if "evaluationIntervalInSeconds" in data:
        out["evaluation_interval_in_seconds"] = data["evaluationIntervalInSeconds"]
    if "missingDataAction" in data:
        import capo_amp.types.anomaly_detector_missing_data_action

        out["missing_data_action"] = (
            capo_amp.types.anomaly_detector_missing_data_action.deserialize_json(
                data["missingDataAction"]
            )
        )
    if "configuration" in data:
        import capo_amp.types.anomaly_detector_configuration

        out["configuration"] = (
            capo_amp.types.anomaly_detector_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "labels" in data:
        import capo_amp.types.prometheus_metric_label_map

        out["labels"] = capo_amp.types.prometheus_metric_label_map.deserialize_json(
            data["labels"]
        )
    if "status" in data:
        import capo_amp.types.anomaly_detector_status

        out["status"] = capo_amp.types.anomaly_detector_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("AnomalyDetectorDescription.status required")
    if "createdAt" in data:
        import capo_amp.types._prelude.timestamp

        out["created_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AnomalyDetectorDescription.created_at required")
    if "modifiedAt" in data:
        import capo_amp.types._prelude.timestamp

        out["modified_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    else:
        raise DeserializationError("AnomalyDetectorDescription.modified_at required")
    if "tags" in data:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.deserialize_json(data["tags"])
    return out
