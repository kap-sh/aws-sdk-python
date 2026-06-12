"""Generated from Smithy shape ``com.amazonaws.rekognition#DisassociateFacesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.disassociated_faces_list
    import aws_sdk_rekognition.types.unsuccessful_face_disassociation_list
    import aws_sdk_rekognition.types.user_status


class DisassociateFacesResponse(TypedDict):
    disassociated_faces: NotRequired[
        "aws_sdk_rekognition.types.disassociated_faces_list.DisassociatedFacesList"
    ]
    """<p>An array of DissociatedFace objects containing FaceIds that are successfully disassociated with the UserID is returned. Returned if the DisassociatedFaces action is successful.</p>"""
    unsuccessful_face_disassociations: NotRequired[
        "aws_sdk_rekognition.types.unsuccessful_face_disassociation_list.UnsuccessfulFaceDisassociationList"
    ]
    """<p>An array of UnsuccessfulDisassociation objects containing FaceIds that are not successfully associated, along with the reasons for the failure to associate. Returned if the DisassociateFaces action is successful.</p>"""
    user_status: NotRequired["aws_sdk_rekognition.types.user_status.UserStatus"]
    """<p>The status of an update made to a User. Reflects if the User has been updated for every requested change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFacesResponse) -> dict:
    out: dict = {}
    if "disassociated_faces" in value:
        import aws_sdk_rekognition.types.disassociated_faces_list

        out["DisassociatedFaces"] = (
            aws_sdk_rekognition.types.disassociated_faces_list.serialize_aws_json_1_1(
                value["disassociated_faces"]
            )
        )
    if "unsuccessful_face_disassociations" in value:
        import aws_sdk_rekognition.types.unsuccessful_face_disassociation_list

        out["UnsuccessfulFaceDisassociations"] = (
            aws_sdk_rekognition.types.unsuccessful_face_disassociation_list.serialize_aws_json_1_1(
                value["unsuccessful_face_disassociations"]
            )
        )
    if "user_status" in value:
        import aws_sdk_rekognition.types.user_status

        out["UserStatus"] = (
            aws_sdk_rekognition.types.user_status.serialize_aws_json_1_1(
                value["user_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFacesResponse:
    out: DisassociateFacesResponse = {}  # type: ignore[typeddict-item]
    if "DisassociatedFaces" in data:
        import aws_sdk_rekognition.types.disassociated_faces_list

        out["disassociated_faces"] = (
            aws_sdk_rekognition.types.disassociated_faces_list.deserialize_aws_json_1_1(
                data["DisassociatedFaces"]
            )
        )
    if "UnsuccessfulFaceDisassociations" in data:
        import aws_sdk_rekognition.types.unsuccessful_face_disassociation_list

        out["unsuccessful_face_disassociations"] = (
            aws_sdk_rekognition.types.unsuccessful_face_disassociation_list.deserialize_aws_json_1_1(
                data["UnsuccessfulFaceDisassociations"]
            )
        )
    if "UserStatus" in data:
        import aws_sdk_rekognition.types.user_status

        out["user_status"] = (
            aws_sdk_rekognition.types.user_status.deserialize_aws_json_1_1(
                data["UserStatus"]
            )
        )
    return out
