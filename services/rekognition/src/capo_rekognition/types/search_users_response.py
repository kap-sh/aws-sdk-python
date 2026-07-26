"""Generated from Smithy shape ``com.amazonaws.rekognition#SearchUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.searched_face
    import capo_rekognition.types.searched_user
    import capo_rekognition.types.string
    import capo_rekognition.types.user_match_list


class SearchUsersResponse(TypedDict, closed=True):
    user_matches: NotRequired["capo_rekognition.types.user_match_list.UserMatchList"]
    """<p>An array of UserMatch objects that matched the input face along with the confidence in the match. Array will be empty if there are no matches.</p>"""
    face_model_version: NotRequired["capo_rekognition.types.string.String"]
    """<p>Version number of the face detection model associated with the input CollectionId.</p>"""
    searched_face: NotRequired["capo_rekognition.types.searched_face.SearchedFace"]
    """<p>Contains the ID of a face that was used to search for matches in a collection.</p>"""
    searched_user: NotRequired["capo_rekognition.types.searched_user.SearchedUser"]
    """<p>Contains the ID of the UserID that was used to search for matches in a collection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchUsersResponse) -> dict:
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
        import capo_rekognition.types.searched_face

        out["SearchedFace"] = (
            capo_rekognition.types.searched_face.serialize_aws_json_1_1(
                value["searched_face"]
            )
        )
    if "searched_user" in value:
        import capo_rekognition.types.searched_user

        out["SearchedUser"] = (
            capo_rekognition.types.searched_user.serialize_aws_json_1_1(
                value["searched_user"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchUsersResponse:
    out: SearchUsersResponse = {}  # type: ignore[typeddict-item]
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
        import capo_rekognition.types.searched_face

        out["searched_face"] = (
            capo_rekognition.types.searched_face.deserialize_aws_json_1_1(
                data["SearchedFace"]
            )
        )
    if "SearchedUser" in data:
        import capo_rekognition.types.searched_user

        out["searched_user"] = (
            capo_rekognition.types.searched_user.deserialize_aws_json_1_1(
                data["SearchedUser"]
            )
        )
    return out
