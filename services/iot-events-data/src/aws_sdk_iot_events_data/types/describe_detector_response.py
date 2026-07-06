"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DescribeDetectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.detector


class DescribeDetectorResponse(TypedDict, closed=True):
    detector: NotRequired["aws_sdk_iot_events_data.types.detector.Detector"]
    """<p>Information about the detector (instance).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDetectorResponse) -> dict:
    out: dict = {}
    if "detector" in value:
        import aws_sdk_iot_events_data.types.detector

        out["detector"] = aws_sdk_iot_events_data.types.detector.serialize_json(
            value["detector"]
        )
    return out


def deserialize_json(data: dict) -> DescribeDetectorResponse:
    out: DescribeDetectorResponse = {}  # type: ignore[typeddict-item]
    if "detector" in data:
        import aws_sdk_iot_events_data.types.detector

        out["detector"] = aws_sdk_iot_events_data.types.detector.deserialize_json(
            data["detector"]
        )
    return out
