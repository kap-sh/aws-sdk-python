"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectionFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.bounding_box_height
    import aws_sdk_rekognition.types.bounding_box_width
    import aws_sdk_rekognition.types.percent


class DetectionFilter(TypedDict):
    min_confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Sets the confidence of word detection. Words with detection confidence below this will be excluded from the result. Values should be between 0 and 100. The default MinConfidence is 80.</p>"""
    min_bounding_box_height: NotRequired[
        "aws_sdk_rekognition.types.bounding_box_height.BoundingBoxHeight"
    ]
    """<p>Sets the minimum height of the word bounding box. Words with bounding box heights lesser than this value will be excluded from the result. Value is relative to the video frame height.</p>"""
    min_bounding_box_width: NotRequired[
        "aws_sdk_rekognition.types.bounding_box_width.BoundingBoxWidth"
    ]
    """<p>Sets the minimum width of the word bounding box. Words with bounding boxes widths lesser than this value will be excluded from the result. Value is relative to the video frame width.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectionFilter) -> dict:
    out: dict = {}
    if "min_confidence" in value:
        out["MinConfidence"] = value["min_confidence"]
    if "min_bounding_box_height" in value:
        out["MinBoundingBoxHeight"] = value["min_bounding_box_height"]
    if "min_bounding_box_width" in value:
        out["MinBoundingBoxWidth"] = value["min_bounding_box_width"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectionFilter:
    out: DetectionFilter = {}  # type: ignore[typeddict-item]
    if "MinConfidence" in data:
        out["min_confidence"] = data["MinConfidence"]
    if "MinBoundingBoxHeight" in data:
        out["min_bounding_box_height"] = data["MinBoundingBoxHeight"]
    if "MinBoundingBoxWidth" in data:
        out["min_bounding_box_width"] = data["MinBoundingBoxWidth"]
    return out
