"""Generated from Smithy shape ``com.amazonaws.rekognition#SearchFacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.face_id
    import capo_rekognition.types.face_match_list
    import capo_rekognition.types.string


class SearchFacesResponse(TypedDict, closed=True):
    searched_face_id: NotRequired["capo_rekognition.types.face_id.FaceId"]
    """<p>ID of the face that was searched for matches in a collection.</p>"""
    face_matches: NotRequired["capo_rekognition.types.face_match_list.FaceMatchList"]
    """<p>An array of faces that matched the input face, along with the confidence in the match.</p>"""
    face_model_version: NotRequired["capo_rekognition.types.string.String"]
    """<p>Version number of the face detection model associated with the input collection (<code>CollectionId</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchFacesResponse) -> dict:
    out: dict = {}
    if "searched_face_id" in value:
        out["SearchedFaceId"] = value["searched_face_id"]
    if "face_matches" in value:
        import capo_rekognition.types.face_match_list

        out["FaceMatches"] = (
            capo_rekognition.types.face_match_list.serialize_aws_json_1_1(
                value["face_matches"]
            )
        )
    if "face_model_version" in value:
        out["FaceModelVersion"] = value["face_model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchFacesResponse:
    out: SearchFacesResponse = {}  # type: ignore[typeddict-item]
    if "SearchedFaceId" in data:
        out["searched_face_id"] = data["SearchedFaceId"]
    if "FaceMatches" in data:
        import capo_rekognition.types.face_match_list

        out["face_matches"] = (
            capo_rekognition.types.face_match_list.deserialize_aws_json_1_1(
                data["FaceMatches"]
            )
        )
    if "FaceModelVersion" in data:
        out["face_model_version"] = data["FaceModelVersion"]
    return out
