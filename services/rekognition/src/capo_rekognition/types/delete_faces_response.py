"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteFacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.face_id_list
    import capo_rekognition.types.unsuccessful_face_deletions_list


class DeleteFacesResponse(TypedDict, closed=True):
    deleted_faces: NotRequired["capo_rekognition.types.face_id_list.FaceIdList"]
    """<p>An array of strings (face IDs) of the faces that were deleted.</p>"""
    unsuccessful_face_deletions: NotRequired[
        "capo_rekognition.types.unsuccessful_face_deletions_list.UnsuccessfulFaceDeletionsList"
    ]
    """<p>An array of any faces that weren't deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFacesResponse) -> dict:
    out: dict = {}
    if "deleted_faces" in value:
        import capo_rekognition.types.face_id_list

        out["DeletedFaces"] = (
            capo_rekognition.types.face_id_list.serialize_aws_json_1_1(
                value["deleted_faces"]
            )
        )
    if "unsuccessful_face_deletions" in value:
        import capo_rekognition.types.unsuccessful_face_deletions_list

        out["UnsuccessfulFaceDeletions"] = (
            capo_rekognition.types.unsuccessful_face_deletions_list.serialize_aws_json_1_1(
                value["unsuccessful_face_deletions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFacesResponse:
    out: DeleteFacesResponse = {}  # type: ignore[typeddict-item]
    if "DeletedFaces" in data:
        import capo_rekognition.types.face_id_list

        out["deleted_faces"] = (
            capo_rekognition.types.face_id_list.deserialize_aws_json_1_1(
                data["DeletedFaces"]
            )
        )
    if "UnsuccessfulFaceDeletions" in data:
        import capo_rekognition.types.unsuccessful_face_deletions_list

        out["unsuccessful_face_deletions"] = (
            capo_rekognition.types.unsuccessful_face_deletions_list.deserialize_aws_json_1_1(
                data["UnsuccessfulFaceDeletions"]
            )
        )
    return out
