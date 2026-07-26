"""Generated from Smithy shape ``com.amazonaws.amp#DescribeAnomalyDetectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.anomaly_detector_description


class DescribeAnomalyDetectorResponse(TypedDict, closed=True):
    anomaly_detector: (
        "capo_amp.types.anomaly_detector_description.AnomalyDetectorDescription"
    )
    """<p>The detailed information about the anomaly detector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAnomalyDetectorResponse) -> dict:
    out: dict = {}
    import capo_amp.types.anomaly_detector_description

    out["anomalyDetector"] = capo_amp.types.anomaly_detector_description.serialize_json(
        value["anomaly_detector"]
    )
    return out


def deserialize_json(data: dict) -> DescribeAnomalyDetectorResponse:
    out: DescribeAnomalyDetectorResponse = {}  # type: ignore[typeddict-item]
    if "anomalyDetector" in data:
        import capo_amp.types.anomaly_detector_description

        out["anomaly_detector"] = (
            capo_amp.types.anomaly_detector_description.deserialize_json(
                data["anomalyDetector"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAnomalyDetectorResponse.anomaly_detector required"
        )
    return out
