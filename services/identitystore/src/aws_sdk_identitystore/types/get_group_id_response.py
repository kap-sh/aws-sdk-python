"""Generated from Smithy shape ``com.amazonaws.identitystore#GetGroupIdResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.resource_id


class GetGroupIdResponse(TypedDict, closed=True):
    group_id: "aws_sdk_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a group in the identity store.</p>"""
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGroupIdResponse) -> dict:
    out: dict = {}
    out["GroupId"] = value["group_id"]
    out["IdentityStoreId"] = value["identity_store_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGroupIdResponse:
    out: GetGroupIdResponse = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("GetGroupIdResponse.group_id required")
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("GetGroupIdResponse.identity_store_id required")
    return out
