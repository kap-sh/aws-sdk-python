"""Generated from Smithy shape ``com.amazonaws.amp#PutAnomalyDetectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.anomaly_detector_arn
    import aws_sdk_amp.types.anomaly_detector_id
    import aws_sdk_amp.types.anomaly_detector_status
    import aws_sdk_amp.types.tag_map


class PutAnomalyDetectorResponse(TypedDict, closed=True):
    anomaly_detector_id: "aws_sdk_amp.types.anomaly_detector_id.AnomalyDetectorId"
    """<p>The unique identifier of the updated anomaly detector.</p>"""
    arn: "aws_sdk_amp.types.anomaly_detector_arn.AnomalyDetectorArn"
    """<p>The Amazon Resource Name (ARN) of the updated anomaly detector.</p>"""
    status: "aws_sdk_amp.types.anomaly_detector_status.AnomalyDetectorStatus"
    """<p>The status information of the updated anomaly detector.</p>"""
    tags: NotRequired["aws_sdk_amp.types.tag_map.TagMap"]
    """<p>The tags applied to the updated anomaly detector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAnomalyDetectorResponse) -> dict:
    out: dict = {}
    out["anomalyDetectorId"] = value["anomaly_detector_id"]
    out["arn"] = value["arn"]
    import aws_sdk_amp.types.anomaly_detector_status

    out["status"] = aws_sdk_amp.types.anomaly_detector_status.serialize_json(
        value["status"]
    )
    if "tags" in value:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PutAnomalyDetectorResponse:
    out: PutAnomalyDetectorResponse = {}  # type: ignore[typeddict-item]
    if "anomalyDetectorId" in data:
        out["anomaly_detector_id"] = data["anomalyDetectorId"]
    else:
        raise DeserializationError(
            "PutAnomalyDetectorResponse.anomaly_detector_id required"
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("PutAnomalyDetectorResponse.arn required")
    if "status" in data:
        import aws_sdk_amp.types.anomaly_detector_status

        out["status"] = aws_sdk_amp.types.anomaly_detector_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("PutAnomalyDetectorResponse.status required")
    if "tags" in data:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.deserialize_json(data["tags"])
    return out
