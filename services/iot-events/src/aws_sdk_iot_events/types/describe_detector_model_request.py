"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeDetectorModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.detector_model_name
    import aws_sdk_iot_events.types.detector_model_version


class DescribeDetectorModelRequest(TypedDict):
    detector_model_name: (
        "aws_sdk_iot_events.types.detector_model_name.DetectorModelName"
    )
    """<p>The name of the detector model.</p>"""
    detector_model_version: NotRequired[
        "aws_sdk_iot_events.types.detector_model_version.DetectorModelVersion"
    ]
    """<p>The version of the detector model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDetectorModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDetectorModelRequest:
    out: DescribeDetectorModelRequest = {}  # type: ignore[typeddict-item]
    return out
