"""Generated from Smithy shape ``com.amazonaws.rekognition#StartShotDetectionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.segment_confidence


class StartShotDetectionFilter(TypedDict, closed=True):
    min_segment_confidence: NotRequired[
        "aws_sdk_rekognition.types.segment_confidence.SegmentConfidence"
    ]
    """<p>Specifies the minimum confidence that Amazon Rekognition Video must have in order to return a detected segment. Confidence represents how certain Amazon Rekognition is that a segment is correctly identified. 0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition Video doesn't return any segments with a confidence level lower than this specified value.</p> <p>If you don't specify <code>MinSegmentConfidence</code>, the <code>GetSegmentDetection</code> returns segments with confidence values greater than or equal to 50 percent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartShotDetectionFilter) -> dict:
    out: dict = {}
    if "min_segment_confidence" in value:
        out["MinSegmentConfidence"] = value["min_segment_confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartShotDetectionFilter:
    out: StartShotDetectionFilter = {}  # type: ignore[typeddict-item]
    if "MinSegmentConfidence" in data:
        out["min_segment_confidence"] = data["MinSegmentConfidence"]
    return out
