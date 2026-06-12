"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DescribeDetectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.detector_model_name
    import aws_sdk_iot_events_data.types.key_value


class DescribeDetectorRequest(TypedDict):
    detector_model_name: (
        "aws_sdk_iot_events_data.types.detector_model_name.DetectorModelName"
    )
    """<p>The name of the detector model whose detectors (instances) you want information about.</p>"""
    key_value: NotRequired["aws_sdk_iot_events_data.types.key_value.KeyValue"]
    """<p>A filter used to limit results to detectors (instances) created because of the given key ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDetectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDetectorRequest:
    out: DescribeDetectorRequest = {}  # type: ignore[typeddict-item]
    return out
