"""Generated from Smithy shape ``com.amazonaws.rekognition#Gender``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.gender_type
    import capo_rekognition.types.percent


class Gender(TypedDict, closed=True):
    value: NotRequired["capo_rekognition.types.gender_type.GenderType"]
    """<p>The predicted gender of the face.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Level of confidence in the prediction.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Gender) -> dict:
    out: dict = {}
    if "value" in value:
        import capo_rekognition.types.gender_type

        out["Value"] = capo_rekognition.types.gender_type.serialize_aws_json_1_1(
            value["value"]
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Gender:
    out: Gender = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        import capo_rekognition.types.gender_type

        out["value"] = capo_rekognition.types.gender_type.deserialize_aws_json_1_1(
            data["Value"]
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
