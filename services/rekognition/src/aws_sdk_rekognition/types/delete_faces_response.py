"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteFacesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face_id_list
    import aws_sdk_rekognition.types.unsuccessful_face_deletions_list


class DeleteFacesResponse(TypedDict):
    deleted_faces: NotRequired["aws_sdk_rekognition.types.face_id_list.FaceIdList"]
    """<p>An array of strings (face IDs) of the faces that were deleted.</p>"""
    unsuccessful_face_deletions: NotRequired[
        "aws_sdk_rekognition.types.unsuccessful_face_deletions_list.UnsuccessfulFaceDeletionsList"
    ]
    """<p>An array of any faces that weren't deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFacesResponse) -> dict:
    out: dict = {}
    if "deleted_faces" in value:
        import aws_sdk_rekognition.types.face_id_list

        out["DeletedFaces"] = (
            aws_sdk_rekognition.types.face_id_list.serialize_aws_json_1_1(
                value["deleted_faces"]
            )
        )
    if "unsuccessful_face_deletions" in value:
        import aws_sdk_rekognition.types.unsuccessful_face_deletions_list

        out["UnsuccessfulFaceDeletions"] = (
            aws_sdk_rekognition.types.unsuccessful_face_deletions_list.serialize_aws_json_1_1(
                value["unsuccessful_face_deletions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFacesResponse:
    out: DeleteFacesResponse = {}  # type: ignore[typeddict-item]
    if "DeletedFaces" in data:
        import aws_sdk_rekognition.types.face_id_list

        out["deleted_faces"] = (
            aws_sdk_rekognition.types.face_id_list.deserialize_aws_json_1_1(
                data["DeletedFaces"]
            )
        )
    if "UnsuccessfulFaceDeletions" in data:
        import aws_sdk_rekognition.types.unsuccessful_face_deletions_list

        out["unsuccessful_face_deletions"] = (
            aws_sdk_rekognition.types.unsuccessful_face_deletions_list.deserialize_aws_json_1_1(
                data["UnsuccessfulFaceDeletions"]
            )
        )
    return out
