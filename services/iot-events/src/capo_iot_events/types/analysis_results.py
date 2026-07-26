"""Generated from Smithy shape ``com.amazonaws.iotevents#AnalysisResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events.types.analysis_result

AnalysisResults: TypeAlias = list[
    "capo_iot_events.types.analysis_result.AnalysisResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisResults) -> list:
    import capo_iot_events.types.analysis_result

    out: list = []
    for item in value:
        out.append(capo_iot_events.types.analysis_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalysisResults:
    import capo_iot_events.types.analysis_result

    out: AnalysisResults = []
    for item in data:
        out.append(capo_iot_events.types.analysis_result.deserialize_json(item))
    return out
