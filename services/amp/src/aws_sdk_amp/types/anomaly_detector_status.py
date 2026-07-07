"""Generated from Smithy shape ``com.amazonaws.amp#AnomalyDetectorStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.anomaly_detector_status_code


class AnomalyDetectorStatus(TypedDict, closed=True):
    status_code: (
        "aws_sdk_amp.types.anomaly_detector_status_code.AnomalyDetectorStatusCode"
    )
    """<p>The status code of the anomaly detector.</p>"""
    status_reason: NotRequired["str"]
    """<p>A description of the current status of the anomaly detector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyDetectorStatus) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.anomaly_detector_status_code

    out["statusCode"] = aws_sdk_amp.types.anomaly_detector_status_code.serialize_json(
        value["status_code"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> AnomalyDetectorStatus:
    out: AnomalyDetectorStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        import aws_sdk_amp.types.anomaly_detector_status_code

        out["status_code"] = (
            aws_sdk_amp.types.anomaly_detector_status_code.deserialize_json(
                data["statusCode"]
            )
        )
    else:
        raise DeserializationError("AnomalyDetectorStatus.status_code required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
