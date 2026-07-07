"""Generated from Smithy shape ``com.amazonaws.identitystore#DeleteUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.resource_id


class DeleteUserRequest(TypedDict, closed=True):
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    user_id: "aws_sdk_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a user in the identity store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["UserId"] = value["user_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserRequest:
    out: DeleteUserRequest = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("DeleteUserRequest.identity_store_id required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("DeleteUserRequest.user_id required")
    return out
