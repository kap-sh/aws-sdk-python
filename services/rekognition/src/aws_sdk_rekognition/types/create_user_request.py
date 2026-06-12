"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.client_request_token
    import aws_sdk_rekognition.types.collection_id
    import aws_sdk_rekognition.types.user_id


class CreateUserRequest(TypedDict):
    collection_id: "aws_sdk_rekognition.types.collection_id.CollectionId"
    """<p>The ID of an existing collection to which the new UserID needs to be created.</p>"""
    user_id: "aws_sdk_rekognition.types.user_id.UserId"
    """<p>ID for the UserID to be created. This ID needs to be unique within the collection.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the request to <code>CreateUser</code>. If you use the same token with multiple <code>CreateUser</code> requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    out["UserId"] = value["user_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("CreateUserRequest.collection_id required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("CreateUserRequest.user_id required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
