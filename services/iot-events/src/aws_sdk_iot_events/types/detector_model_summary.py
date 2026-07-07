"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.detector_model_description
    import aws_sdk_iot_events.types.detector_model_name
    import aws_sdk_iot_events.types.timestamp


class DetectorModelSummary(TypedDict, closed=True):
    detector_model_name: NotRequired[
        "aws_sdk_iot_events.types.detector_model_name.DetectorModelName"
    ]
    """<p>The name of the detector model.</p>"""
    detector_model_description: NotRequired[
        "aws_sdk_iot_events.types.detector_model_description.DetectorModelDescription"
    ]
    """<p>A brief description of the detector model.</p>"""
    creation_time: NotRequired["aws_sdk_iot_events.types.timestamp.Timestamp"]
    """<p>The time the detector model was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorModelSummary) -> dict:
    out: dict = {}
    if "detector_model_name" in value:
        out["detectorModelName"] = value["detector_model_name"]
    if "detector_model_description" in value:
        out["detectorModelDescription"] = value["detector_model_description"]
    if "creation_time" in value:
        import aws_sdk_iot_events.types.timestamp

        out["creationTime"] = aws_sdk_iot_events.types.timestamp.serialize_json(
            value["creation_time"]
        )
    return out


def deserialize_json(data: dict) -> DetectorModelSummary:
    out: DetectorModelSummary = {}  # type: ignore[typeddict-item]
    if "detectorModelName" in data:
        out["detector_model_name"] = data["detectorModelName"]
    if "detectorModelDescription" in data:
        out["detector_model_description"] = data["detectorModelDescription"]
    if "creationTime" in data:
        import aws_sdk_iot_events.types.timestamp

        out["creation_time"] = aws_sdk_iot_events.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    return out
