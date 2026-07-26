"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorModelSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events.types.detector_model_summary

DetectorModelSummaries: TypeAlias = list[
    "capo_iot_events.types.detector_model_summary.DetectorModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorModelSummaries) -> list:
    import capo_iot_events.types.detector_model_summary

    out: list = []
    for item in value:
        out.append(capo_iot_events.types.detector_model_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DetectorModelSummaries:
    import capo_iot_events.types.detector_model_summary

    out: DetectorModelSummaries = []
    for item in data:
        out.append(capo_iot_events.types.detector_model_summary.deserialize_json(item))
    return out
