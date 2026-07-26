"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeDetectorModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.detector_model_name
    import capo_iot_events.types.detector_model_version


class DescribeDetectorModelRequest(TypedDict, closed=True):
    detector_model_name: "capo_iot_events.types.detector_model_name.DetectorModelName"
    """<p>The name of the detector model.</p>"""
    detector_model_version: NotRequired[
        "capo_iot_events.types.detector_model_version.DetectorModelVersion"
    ]
    """<p>The version of the detector model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDetectorModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDetectorModelRequest:
    out: DescribeDetectorModelRequest = {}  # type: ignore[typeddict-item]
    return out
