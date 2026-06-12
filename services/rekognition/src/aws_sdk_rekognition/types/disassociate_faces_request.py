"""Generated from Smithy shape ``com.amazonaws.rekognition#DisassociateFacesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.client_request_token
    import aws_sdk_rekognition.types.collection_id
    import aws_sdk_rekognition.types.user_face_id_list
    import aws_sdk_rekognition.types.user_id


class DisassociateFacesRequest(TypedDict):
    collection_id: "aws_sdk_rekognition.types.collection_id.CollectionId"
    """<p>The ID of an existing collection containing the UserID.</p>"""
    user_id: "aws_sdk_rekognition.types.user_id.UserId"
    """<p>ID for the existing UserID.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the request to <code>DisassociateFaces</code>. If you use the same token with multiple <code>DisassociateFaces</code> requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.</p>"""
    face_ids: "aws_sdk_rekognition.types.user_face_id_list.UserFaceIdList"
    """<p>An array of face IDs to disassociate from the UserID. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFacesRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    out["UserId"] = value["user_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    import aws_sdk_rekognition.types.user_face_id_list

    out["FaceIds"] = aws_sdk_rekognition.types.user_face_id_list.serialize_aws_json_1_1(
        value["face_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFacesRequest:
    out: DisassociateFacesRequest = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("DisassociateFacesRequest.collection_id required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("DisassociateFacesRequest.user_id required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "FaceIds" in data:
        import aws_sdk_rekognition.types.user_face_id_list

        out["face_ids"] = (
            aws_sdk_rekognition.types.user_face_id_list.deserialize_aws_json_1_1(
                data["FaceIds"]
            )
        )
    else:
        raise DeserializationError("DisassociateFacesRequest.face_ids required")
    return out
