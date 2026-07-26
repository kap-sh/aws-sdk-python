"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeDetectorModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.detector_model


class DescribeDetectorModelResponse(TypedDict, closed=True):
    detector_model: NotRequired["capo_iot_events.types.detector_model.DetectorModel"]
    """<p>Information about the detector model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDetectorModelResponse) -> dict:
    out: dict = {}
    if "detector_model" in value:
        import capo_iot_events.types.detector_model

        out["detectorModel"] = capo_iot_events.types.detector_model.serialize_json(
            value["detector_model"]
        )
    return out


def deserialize_json(data: dict) -> DescribeDetectorModelResponse:
    out: DescribeDetectorModelResponse = {}  # type: ignore[typeddict-item]
    if "detectorModel" in data:
        import capo_iot_events.types.detector_model

        out["detector_model"] = capo_iot_events.types.detector_model.deserialize_json(
            data["detectorModel"]
        )
    return out
