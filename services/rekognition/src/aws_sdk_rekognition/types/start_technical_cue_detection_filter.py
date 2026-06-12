"""Generated from Smithy shape ``com.amazonaws.rekognition#StartTechnicalCueDetectionFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.black_frame
    import aws_sdk_rekognition.types.segment_confidence


class StartTechnicalCueDetectionFilter(TypedDict):
    min_segment_confidence: NotRequired[
        "aws_sdk_rekognition.types.segment_confidence.SegmentConfidence"
    ]
    """<p>Specifies the minimum confidence that Amazon Rekognition Video must have in order to return a detected segment. Confidence represents how certain Amazon Rekognition is that a segment is correctly identified. 0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition Video doesn't return any segments with a confidence level lower than this specified value.</p> <p>If you don't specify <code>MinSegmentConfidence</code>, <code>GetSegmentDetection</code> returns segments with confidence values greater than or equal to 50 percent.</p>"""
    black_frame: NotRequired["aws_sdk_rekognition.types.black_frame.BlackFrame"]
    """<p> A filter that allows you to control the black frame detection by specifying the black levels and pixel coverage of black pixels in a frame. Videos can come from multiple sources, formats, and time periods, with different standards and varying noise levels for black frames that need to be accounted for. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTechnicalCueDetectionFilter) -> dict:
    out: dict = {}
    if "min_segment_confidence" in value:
        out["MinSegmentConfidence"] = value["min_segment_confidence"]
    if "black_frame" in value:
        import aws_sdk_rekognition.types.black_frame

        out["BlackFrame"] = (
            aws_sdk_rekognition.types.black_frame.serialize_aws_json_1_1(
                value["black_frame"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTechnicalCueDetectionFilter:
    out: StartTechnicalCueDetectionFilter = {}  # type: ignore[typeddict-item]
    if "MinSegmentConfidence" in data:
        out["min_segment_confidence"] = data["MinSegmentConfidence"]
    if "BlackFrame" in data:
        import aws_sdk_rekognition.types.black_frame

        out["black_frame"] = (
            aws_sdk_rekognition.types.black_frame.deserialize_aws_json_1_1(
                data["BlackFrame"]
            )
        )
    return out
