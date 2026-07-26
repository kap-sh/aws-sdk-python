"""Generated from Smithy shape ``com.amazonaws.rekognition#SearchUsersByImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.searched_face_details
    import capo_rekognition.types.string
    import capo_rekognition.types.unsearched_faces_list
    import capo_rekognition.types.user_match_list


class SearchUsersByImageResponse(TypedDict, closed=True):
    user_matches: NotRequired["capo_rekognition.types.user_match_list.UserMatchList"]
    """<p>An array of UserID objects that matched the input face, along with the confidence in the match. The returned structure will be empty if there are no matches. Returned if the SearchUsersByImageResponse action is successful.</p>"""
    face_model_version: NotRequired["capo_rekognition.types.string.String"]
    """<p>Version number of the face detection model associated with the input collection CollectionId.</p>"""
    searched_face: NotRequired[
        "capo_rekognition.types.searched_face_details.SearchedFaceDetails"
    ]
    """<p>A list of FaceDetail objects containing the BoundingBox for the largest face in image, as well as the confidence in the bounding box, that was searched for matches. If no valid face is detected in the image the response will contain no SearchedFace object.</p>"""
    unsearched_faces: NotRequired[
        "capo_rekognition.types.unsearched_faces_list.UnsearchedFacesList"
    ]
    """<p>List of UnsearchedFace objects. Contains the face details infered from the specified image but not used for search. Contains reasons that describe why a face wasn't used for Search. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchUsersByImageResponse) -> dict:
    out: dict = {}
    if "user_matches" in value:
        import capo_rekognition.types.user_match_list

        out["UserMatches"] = (
            capo_rekognition.types.user_match_list.serialize_aws_json_1_1(
                value["user_matches"]
            )
        )
    if "face_model_version" in value:
        out["FaceModelVersion"] = value["face_model_version"]
    if "searched_face" in value:
        import capo_rekognition.types.searched_face_details

        out["SearchedFace"] = (
            capo_rekognition.types.searched_face_details.serialize_aws_json_1_1(
                value["searched_face"]
            )
        )
    if "unsearched_faces" in value:
        import capo_rekognition.types.unsearched_faces_list

        out["UnsearchedFaces"] = (
            capo_rekognition.types.unsearched_faces_list.serialize_aws_json_1_1(
                value["unsearched_faces"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchUsersByImageResponse:
    out: SearchUsersByImageResponse = {}  # type: ignore[typeddict-item]
    if "UserMatches" in data:
        import capo_rekognition.types.user_match_list

        out["user_matches"] = (
            capo_rekognition.types.user_match_list.deserialize_aws_json_1_1(
                data["UserMatches"]
            )
        )
    if "FaceModelVersion" in data:
        out["face_model_version"] = data["FaceModelVersion"]
    if "SearchedFace" in data:
        import capo_rekognition.types.searched_face_details

        out["searched_face"] = (
            capo_rekognition.types.searched_face_details.deserialize_aws_json_1_1(
                data["SearchedFace"]
            )
        )
    if "UnsearchedFaces" in data:
        import capo_rekognition.types.unsearched_faces_list

        out["unsearched_faces"] = (
            capo_rekognition.types.unsearched_faces_list.deserialize_aws_json_1_1(
                data["UnsearchedFaces"]
            )
        )
    return out
