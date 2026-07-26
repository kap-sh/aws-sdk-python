"""Generated from Smithy shape ``com.amazonaws.identitystore#DeleteGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.resource_id


class DeleteGroupRequest(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    group_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a group in the identity store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGroupRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["GroupId"] = value["group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGroupRequest:
    out: DeleteGroupRequest = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("DeleteGroupRequest.identity_store_id required")
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("DeleteGroupRequest.group_id required")
    return out
