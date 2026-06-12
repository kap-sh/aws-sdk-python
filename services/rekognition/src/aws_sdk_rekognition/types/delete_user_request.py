"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.client_request_token
    import aws_sdk_rekognition.types.collection_id
    import aws_sdk_rekognition.types.user_id


class DeleteUserRequest(TypedDict):
    collection_id: "aws_sdk_rekognition.types.collection_id.CollectionId"
    """<p>The ID of an existing collection from which the UserID needs to be deleted. </p>"""
    user_id: "aws_sdk_rekognition.types.user_id.UserId"
    """<p>ID for the UserID to be deleted. </p>"""
    client_request_token: NotRequired[
        "aws_sdk_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the request to <code>DeleteUser</code>. If you use the same token with multiple <code>DeleteUser </code>requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    out["UserId"] = value["user_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserRequest:
    out: DeleteUserRequest = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("DeleteUserRequest.collection_id required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("DeleteUserRequest.user_id required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
