"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceMatch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face
    import aws_sdk_rekognition.types.percent


class FaceMatch(TypedDict):
    similarity: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Confidence in the match of this face with the input face.</p>"""
    face: NotRequired["aws_sdk_rekognition.types.face.Face"]
    """<p>Describes the face properties such as the bounding box, face ID, image ID of the source image, and external image ID that you assigned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceMatch) -> dict:
    out: dict = {}
    if "similarity" in value:
        out["Similarity"] = value["similarity"]
    if "face" in value:
        import aws_sdk_rekognition.types.face

        out["Face"] = aws_sdk_rekognition.types.face.serialize_aws_json_1_1(
            value["face"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FaceMatch:
    out: FaceMatch = {}  # type: ignore[typeddict-item]
    if "Similarity" in data:
        out["similarity"] = data["Similarity"]
    if "Face" in data:
        import aws_sdk_rekognition.types.face

        out["face"] = aws_sdk_rekognition.types.face.deserialize_aws_json_1_1(
            data["Face"]
        )
    return out
