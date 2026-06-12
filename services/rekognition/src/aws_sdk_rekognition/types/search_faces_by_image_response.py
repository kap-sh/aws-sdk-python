"""Generated from Smithy shape ``com.amazonaws.rekognition#SearchFacesByImageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.bounding_box
    import aws_sdk_rekognition.types.face_match_list
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.string


class SearchFacesByImageResponse(TypedDict):
    searched_face_bounding_box: NotRequired[
        "aws_sdk_rekognition.types.bounding_box.BoundingBox"
    ]
    """<p>The bounding box around the face in the input image that Amazon Rekognition used for the search.</p>"""
    searched_face_confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The level of confidence that the <code>searchedFaceBoundingBox</code>, contains a face.</p>"""
    face_matches: NotRequired["aws_sdk_rekognition.types.face_match_list.FaceMatchList"]
    """<p>An array of faces that match the input face, along with the confidence in the match.</p>"""
    face_model_version: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>Version number of the face detection model associated with the input collection (<code>CollectionId</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchFacesByImageResponse) -> dict:
    out: dict = {}
    if "searched_face_bounding_box" in value:
        import aws_sdk_rekognition.types.bounding_box

        out["SearchedFaceBoundingBox"] = (
            aws_sdk_rekognition.types.bounding_box.serialize_aws_json_1_1(
                value["searched_face_bounding_box"]
            )
        )
    if "searched_face_confidence" in value:
        out["SearchedFaceConfidence"] = value["searched_face_confidence"]
    if "face_matches" in value:
        import aws_sdk_rekognition.types.face_match_list

        out["FaceMatches"] = (
            aws_sdk_rekognition.types.face_match_list.serialize_aws_json_1_1(
                value["face_matches"]
            )
        )
    if "face_model_version" in value:
        out["FaceModelVersion"] = value["face_model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchFacesByImageResponse:
    out: SearchFacesByImageResponse = {}  # type: ignore[typeddict-item]
    if "SearchedFaceBoundingBox" in data:
        import aws_sdk_rekognition.types.bounding_box

        out["searched_face_bounding_box"] = (
            aws_sdk_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["SearchedFaceBoundingBox"]
            )
        )
    if "SearchedFaceConfidence" in data:
        out["searched_face_confidence"] = data["SearchedFaceConfidence"]
    if "FaceMatches" in data:
        import aws_sdk_rekognition.types.face_match_list

        out["face_matches"] = (
            aws_sdk_rekognition.types.face_match_list.deserialize_aws_json_1_1(
                data["FaceMatches"]
            )
        )
    if "FaceModelVersion" in data:
        out["face_model_version"] = data["FaceModelVersion"]
    return out
