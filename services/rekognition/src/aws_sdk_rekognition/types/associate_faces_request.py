"""Generated from Smithy shape ``com.amazonaws.rekognition#AssociateFacesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.client_request_token
    import aws_sdk_rekognition.types.collection_id
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.user_face_id_list
    import aws_sdk_rekognition.types.user_id


class AssociateFacesRequest(TypedDict):
    collection_id: "aws_sdk_rekognition.types.collection_id.CollectionId"
    """<p>The ID of an existing collection containing the UserID.</p>"""
    user_id: "aws_sdk_rekognition.types.user_id.UserId"
    """<p>The ID for the existing UserID.</p>"""
    face_ids: "aws_sdk_rekognition.types.user_face_id_list.UserFaceIdList"
    """<p>An array of FaceIDs to associate with the UserID.</p>"""
    user_match_threshold: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>An optional value specifying the minimum confidence in the UserID match to return. The default value is 75.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the request to <code>AssociateFaces</code>. If you use the same token with multiple <code>AssociateFaces</code> requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateFacesRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    out["UserId"] = value["user_id"]
    import aws_sdk_rekognition.types.user_face_id_list

    out["FaceIds"] = aws_sdk_rekognition.types.user_face_id_list.serialize_aws_json_1_1(
        value["face_ids"]
    )
    if "user_match_threshold" in value:
        out["UserMatchThreshold"] = value["user_match_threshold"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateFacesRequest:
    out: AssociateFacesRequest = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("AssociateFacesRequest.collection_id required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("AssociateFacesRequest.user_id required")
    if "FaceIds" in data:
        import aws_sdk_rekognition.types.user_face_id_list

        out["face_ids"] = (
            aws_sdk_rekognition.types.user_face_id_list.deserialize_aws_json_1_1(
                data["FaceIds"]
            )
        )
    else:
        raise DeserializationError("AssociateFacesRequest.face_ids required")
    if "UserMatchThreshold" in data:
        out["user_match_threshold"] = data["UserMatchThreshold"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
