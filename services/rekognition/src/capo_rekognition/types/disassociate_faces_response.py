"""Generated from Smithy shape ``com.amazonaws.rekognition#DisassociateFacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.disassociated_faces_list
    import capo_rekognition.types.unsuccessful_face_disassociation_list
    import capo_rekognition.types.user_status


class DisassociateFacesResponse(TypedDict, closed=True):
    disassociated_faces: NotRequired[
        "capo_rekognition.types.disassociated_faces_list.DisassociatedFacesList"
    ]
    """<p>An array of DissociatedFace objects containing FaceIds that are successfully disassociated with the UserID is returned. Returned if the DisassociatedFaces action is successful.</p>"""
    unsuccessful_face_disassociations: NotRequired[
        "capo_rekognition.types.unsuccessful_face_disassociation_list.UnsuccessfulFaceDisassociationList"
    ]
    """<p>An array of UnsuccessfulDisassociation objects containing FaceIds that are not successfully associated, along with the reasons for the failure to associate. Returned if the DisassociateFaces action is successful.</p>"""
    user_status: NotRequired["capo_rekognition.types.user_status.UserStatus"]
    """<p>The status of an update made to a User. Reflects if the User has been updated for every requested change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFacesResponse) -> dict:
    out: dict = {}
    if "disassociated_faces" in value:
        import capo_rekognition.types.disassociated_faces_list

        out["DisassociatedFaces"] = (
            capo_rekognition.types.disassociated_faces_list.serialize_aws_json_1_1(
                value["disassociated_faces"]
            )
        )
    if "unsuccessful_face_disassociations" in value:
        import capo_rekognition.types.unsuccessful_face_disassociation_list

        out["UnsuccessfulFaceDisassociations"] = (
            capo_rekognition.types.unsuccessful_face_disassociation_list.serialize_aws_json_1_1(
                value["unsuccessful_face_disassociations"]
            )
        )
    if "user_status" in value:
        import capo_rekognition.types.user_status

        out["UserStatus"] = capo_rekognition.types.user_status.serialize_aws_json_1_1(
            value["user_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFacesResponse:
    out: DisassociateFacesResponse = {}  # type: ignore[typeddict-item]
    if "DisassociatedFaces" in data:
        import capo_rekognition.types.disassociated_faces_list

        out["disassociated_faces"] = (
            capo_rekognition.types.disassociated_faces_list.deserialize_aws_json_1_1(
                data["DisassociatedFaces"]
            )
        )
    if "UnsuccessfulFaceDisassociations" in data:
        import capo_rekognition.types.unsuccessful_face_disassociation_list

        out["unsuccessful_face_disassociations"] = (
            capo_rekognition.types.unsuccessful_face_disassociation_list.deserialize_aws_json_1_1(
                data["UnsuccessfulFaceDisassociations"]
            )
        )
    if "UserStatus" in data:
        import capo_rekognition.types.user_status

        out["user_status"] = (
            capo_rekognition.types.user_status.deserialize_aws_json_1_1(
                data["UserStatus"]
            )
        )
    return out
