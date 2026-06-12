"""Generated from Smithy shape ``com.amazonaws.rekognition#TechnicalCueSegment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.segment_confidence
    import aws_sdk_rekognition.types.technical_cue_type


class TechnicalCueSegment(TypedDict):
    type: NotRequired["aws_sdk_rekognition.types.technical_cue_type.TechnicalCueType"]
    """<p>The type of the technical cue.</p>"""
    confidence: NotRequired[
        "aws_sdk_rekognition.types.segment_confidence.SegmentConfidence"
    ]
    """<p>The confidence that Amazon Rekognition Video has in the accuracy of the detected segment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TechnicalCueSegment) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_rekognition.types.technical_cue_type

        out["Type"] = (
            aws_sdk_rekognition.types.technical_cue_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TechnicalCueSegment:
    out: TechnicalCueSegment = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_rekognition.types.technical_cue_type

        out["type"] = (
            aws_sdk_rekognition.types.technical_cue_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
