"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DetectorSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events_data.types.detector_summary

DetectorSummaries: TypeAlias = list[
    "capo_iot_events_data.types.detector_summary.DetectorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorSummaries) -> list:
    import capo_iot_events_data.types.detector_summary

    out: list = []
    for item in value:
        out.append(capo_iot_events_data.types.detector_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DetectorSummaries:
    import capo_iot_events_data.types.detector_summary

    out: DetectorSummaries = []
    for item in data:
        out.append(capo_iot_events_data.types.detector_summary.deserialize_json(item))
    return out
