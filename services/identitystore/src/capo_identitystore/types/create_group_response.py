"""Generated from Smithy shape ``com.amazonaws.identitystore#CreateGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.resource_id


class CreateGroupResponse(TypedDict, closed=True):
    group_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier of the newly created group in the identity store.</p>"""
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGroupResponse) -> dict:
    out: dict = {}
    out["GroupId"] = value["group_id"]
    out["IdentityStoreId"] = value["identity_store_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGroupResponse:
    out: CreateGroupResponse = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("CreateGroupResponse.group_id required")
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("CreateGroupResponse.identity_store_id required")
    return out
