"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorModelVersionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.detector_model_version_summary

DetectorModelVersionSummaries: TypeAlias = list[
    "aws_sdk_iot_events.types.detector_model_version_summary.DetectorModelVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorModelVersionSummaries) -> list:
    import aws_sdk_iot_events.types.detector_model_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_events.types.detector_model_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DetectorModelVersionSummaries:
    import aws_sdk_iot_events.types.detector_model_version_summary

    out: DetectorModelVersionSummaries = []
    for item in data:
        out.append(
            aws_sdk_iot_events.types.detector_model_version_summary.deserialize_json(
                item
            )
        )
    return out
