"""Generated from Smithy shape ``com.amazonaws.rekognition#TechnicalCueSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.segment_confidence
    import capo_rekognition.types.technical_cue_type


class TechnicalCueSegment(TypedDict, closed=True):
    type: NotRequired["capo_rekognition.types.technical_cue_type.TechnicalCueType"]
    """<p>The type of the technical cue.</p>"""
    confidence: NotRequired[
        "capo_rekognition.types.segment_confidence.SegmentConfidence"
    ]
    """<p>The confidence that Amazon Rekognition Video has in the accuracy of the detected segment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TechnicalCueSegment) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_rekognition.types.technical_cue_type

        out["Type"] = capo_rekognition.types.technical_cue_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TechnicalCueSegment:
    out: TechnicalCueSegment = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_rekognition.types.technical_cue_type

        out["type"] = (
            capo_rekognition.types.technical_cue_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
