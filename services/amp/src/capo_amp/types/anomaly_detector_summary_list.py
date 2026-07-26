"""Generated from Smithy shape ``com.amazonaws.amp#AnomalyDetectorSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amp.types.anomaly_detector_summary

AnomalyDetectorSummaryList: TypeAlias = list[
    "capo_amp.types.anomaly_detector_summary.AnomalyDetectorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyDetectorSummaryList) -> list:
    import capo_amp.types.anomaly_detector_summary

    out: list = []
    for item in value:
        out.append(capo_amp.types.anomaly_detector_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnomalyDetectorSummaryList:
    import capo_amp.types.anomaly_detector_summary

    out: AnomalyDetectorSummaryList = []
    for item in data:
        out.append(capo_amp.types.anomaly_detector_summary.deserialize_json(item))
    return out
