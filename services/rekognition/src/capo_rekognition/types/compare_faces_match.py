"""Generated from Smithy shape ``com.amazonaws.rekognition#CompareFacesMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.compared_face
    import capo_rekognition.types.percent


class CompareFacesMatch(TypedDict, closed=True):
    similarity: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Level of confidence that the faces match.</p>"""
    face: NotRequired["capo_rekognition.types.compared_face.ComparedFace"]
    """<p>Provides face metadata (bounding box and confidence that the bounding box actually contains a face).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompareFacesMatch) -> dict:
    out: dict = {}
    if "similarity" in value:
        out["Similarity"] = value["similarity"]
    if "face" in value:
        import capo_rekognition.types.compared_face

        out["Face"] = capo_rekognition.types.compared_face.serialize_aws_json_1_1(
            value["face"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompareFacesMatch:
    out: CompareFacesMatch = {}  # type: ignore[typeddict-item]
    if "Similarity" in data:
        out["similarity"] = data["Similarity"]
    if "Face" in data:
        import capo_rekognition.types.compared_face

        out["face"] = capo_rekognition.types.compared_face.deserialize_aws_json_1_1(
            data["Face"]
        )
    return out
