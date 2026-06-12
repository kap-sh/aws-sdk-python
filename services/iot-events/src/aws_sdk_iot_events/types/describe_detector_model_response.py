"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeDetectorModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.detector_model


class DescribeDetectorModelResponse(TypedDict):
    detector_model: NotRequired["aws_sdk_iot_events.types.detector_model.DetectorModel"]
    """<p>Information about the detector model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDetectorModelResponse) -> dict:
    out: dict = {}
    if "detector_model" in value:
        import aws_sdk_iot_events.types.detector_model

        out["detectorModel"] = aws_sdk_iot_events.types.detector_model.serialize_json(
            value["detector_model"]
        )
    return out


def deserialize_json(data: dict) -> DescribeDetectorModelResponse:
    out: DescribeDetectorModelResponse = {}  # type: ignore[typeddict-item]
    if "detectorModel" in data:
        import aws_sdk_iot_events.types.detector_model

        out["detector_model"] = (
            aws_sdk_iot_events.types.detector_model.deserialize_json(
                data["detectorModel"]
            )
        )
    return out
