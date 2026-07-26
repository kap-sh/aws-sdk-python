"""Generated from Smithy shape ``com.amazonaws.identitystore#CreateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.group_display_name
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.sensitive_string_type


class CreateGroupRequest(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    display_name: NotRequired[
        "capo_identitystore.types.group_display_name.GroupDisplayName"
    ]
    """<p>A string containing the name of the group. This value is commonly displayed when the group is referenced. <code>Administrator</code> and <code>AWSAdministrators</code> are reserved names and can't be used for users or groups.</p>"""
    description: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing the description of the group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGroupRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGroupRequest:
    out: CreateGroupRequest = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("CreateGroupRequest.identity_store_id required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
