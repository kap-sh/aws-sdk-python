"""Generated from Smithy shape ``com.amazonaws.iotevents#AnalysisResultLocations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.analysis_result_location

AnalysisResultLocations: TypeAlias = list[
    "aws_sdk_iot_events.types.analysis_result_location.AnalysisResultLocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisResultLocations) -> list:
    import aws_sdk_iot_events.types.analysis_result_location

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_events.types.analysis_result_location.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalysisResultLocations:
    import aws_sdk_iot_events.types.analysis_result_location

    out: AnalysisResultLocations = []
    for item in data:
        out.append(
            aws_sdk_iot_events.types.analysis_result_location.deserialize_json(item)
        )
    return out
