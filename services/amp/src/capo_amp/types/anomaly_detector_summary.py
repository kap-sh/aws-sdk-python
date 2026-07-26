"""Generated from Smithy shape ``com.amazonaws.amp#AnomalyDetectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_amp.types.anomaly_detector_alias
    import capo_amp.types.anomaly_detector_arn
    import capo_amp.types.anomaly_detector_id
    import capo_amp.types.anomaly_detector_status
    import capo_amp.types.tag_map


class AnomalyDetectorSummary(TypedDict, closed=True):
    arn: "capo_amp.types.anomaly_detector_arn.AnomalyDetectorArn"
    """<p>The Amazon Resource Name (ARN) of the anomaly detector.</p>"""
    anomaly_detector_id: "capo_amp.types.anomaly_detector_id.AnomalyDetectorId"
    """<p>The unique identifier of the anomaly detector.</p>"""
    alias: "capo_amp.types.anomaly_detector_alias.AnomalyDetectorAlias"
    """<p>The user-friendly name of the anomaly detector.</p>"""
    status: "capo_amp.types.anomaly_detector_status.AnomalyDetectorStatus"
    """<p>The current status of the anomaly detector.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the anomaly detector was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The timestamp when the anomaly detector was last modified.</p>"""
    tags: NotRequired["capo_amp.types.tag_map.TagMap"]
    """<p>The tags applied to the anomaly detector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyDetectorSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["anomalyDetectorId"] = value["anomaly_detector_id"]
    out["alias"] = value["alias"]
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


def deserialize_json(data: dict) -> AnomalyDetectorSummary:
    out: AnomalyDetectorSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AnomalyDetectorSummary.arn required")
    if "anomalyDetectorId" in data:
        out["anomaly_detector_id"] = data["anomalyDetectorId"]
    else:
        raise DeserializationError(
            "AnomalyDetectorSummary.anomaly_detector_id required"
        )
    if "alias" in data:
        out["alias"] = data["alias"]
    else:
        raise DeserializationError("AnomalyDetectorSummary.alias required")
    if "status" in data:
        import capo_amp.types.anomaly_detector_status

        out["status"] = capo_amp.types.anomaly_detector_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("AnomalyDetectorSummary.status required")
    if "createdAt" in data:
        import capo_amp.types._prelude.timestamp

        out["created_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AnomalyDetectorSummary.created_at required")
    if "modifiedAt" in data:
        import capo_amp.types._prelude.timestamp

        out["modified_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    else:
        raise DeserializationError("AnomalyDetectorSummary.modified_at required")
    if "tags" in data:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.deserialize_json(data["tags"])
    return out
