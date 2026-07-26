"""Generated from Smithy shape ``com.amazonaws.rekognition#AssociateFacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.associated_faces_list
    import capo_rekognition.types.unsuccessful_face_association_list
    import capo_rekognition.types.user_status


class AssociateFacesResponse(TypedDict, closed=True):
    associated_faces: NotRequired[
        "capo_rekognition.types.associated_faces_list.AssociatedFacesList"
    ]
    """<p>An array of AssociatedFace objects containing FaceIDs that have been successfully associated with the UserID. Returned if the AssociateFaces action is successful.</p>"""
    unsuccessful_face_associations: NotRequired[
        "capo_rekognition.types.unsuccessful_face_association_list.UnsuccessfulFaceAssociationList"
    ]
    """<p>An array of UnsuccessfulAssociation objects containing FaceIDs that are not successfully associated along with the reasons. Returned if the AssociateFaces action is successful.</p>"""
    user_status: NotRequired["capo_rekognition.types.user_status.UserStatus"]
    """<p>The status of an update made to a UserID. Reflects if the UserID has been updated for every requested change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateFacesResponse) -> dict:
    out: dict = {}
    if "associated_faces" in value:
        import capo_rekognition.types.associated_faces_list

        out["AssociatedFaces"] = (
            capo_rekognition.types.associated_faces_list.serialize_aws_json_1_1(
                value["associated_faces"]
            )
        )
    if "unsuccessful_face_associations" in value:
        import capo_rekognition.types.unsuccessful_face_association_list

        out["UnsuccessfulFaceAssociations"] = (
            capo_rekognition.types.unsuccessful_face_association_list.serialize_aws_json_1_1(
                value["unsuccessful_face_associations"]
            )
        )
    if "user_status" in value:
        import capo_rekognition.types.user_status

        out["UserStatus"] = capo_rekognition.types.user_status.serialize_aws_json_1_1(
            value["user_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateFacesResponse:
    out: AssociateFacesResponse = {}  # type: ignore[typeddict-item]
    if "AssociatedFaces" in data:
        import capo_rekognition.types.associated_faces_list

        out["associated_faces"] = (
            capo_rekognition.types.associated_faces_list.deserialize_aws_json_1_1(
                data["AssociatedFaces"]
            )
        )
    if "UnsuccessfulFaceAssociations" in data:
        import capo_rekognition.types.unsuccessful_face_association_list

        out["unsuccessful_face_associations"] = (
            capo_rekognition.types.unsuccessful_face_association_list.deserialize_aws_json_1_1(
                data["UnsuccessfulFaceAssociations"]
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
