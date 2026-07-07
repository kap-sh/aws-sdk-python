"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteFacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.collection_id
    import aws_sdk_rekognition.types.face_id_list


class DeleteFacesRequest(TypedDict, closed=True):
    collection_id: "aws_sdk_rekognition.types.collection_id.CollectionId"
    """<p>Collection from which to remove the specific faces.</p>"""
    face_ids: "aws_sdk_rekognition.types.face_id_list.FaceIdList"
    """<p>An array of face IDs to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFacesRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    import aws_sdk_rekognition.types.face_id_list

    out["FaceIds"] = aws_sdk_rekognition.types.face_id_list.serialize_aws_json_1_1(
        value["face_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFacesRequest:
    out: DeleteFacesRequest = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("DeleteFacesRequest.collection_id required")
    if "FaceIds" in data:
        import aws_sdk_rekognition.types.face_id_list

        out["face_ids"] = (
            aws_sdk_rekognition.types.face_id_list.deserialize_aws_json_1_1(
                data["FaceIds"]
            )
        )
    else:
        raise DeserializationError("DeleteFacesRequest.face_ids required")
    return out
