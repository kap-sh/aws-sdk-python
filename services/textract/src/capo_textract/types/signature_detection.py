"""Generated from Smithy shape ``com.amazonaws.textract#SignatureDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.geometry
    import capo_textract.types.percent


class SignatureDetection(TypedDict, closed=True):
    confidence: NotRequired["capo_textract.types.percent.Percent"]
    """<p>The confidence, from 0 to 100, in the predicted values for a detected signature.</p>"""
    geometry: NotRequired["capo_textract.types.geometry.Geometry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SignatureDetection) -> dict:
    out: dict = {}
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "geometry" in value:
        import capo_textract.types.geometry

        out["Geometry"] = capo_textract.types.geometry.serialize_aws_json_1_1(
            value["geometry"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SignatureDetection:
    out: SignatureDetection = {}  # type: ignore[typeddict-item]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Geometry" in data:
        import capo_textract.types.geometry

        out["geometry"] = capo_textract.types.geometry.deserialize_aws_json_1_1(
            data["Geometry"]
        )
    return out
