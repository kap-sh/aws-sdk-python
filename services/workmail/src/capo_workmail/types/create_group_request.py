"""Generated from Smithy shape ``com.amazonaws.workmail#CreateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.boolean
    import capo_workmail.types.group_name
    import capo_workmail.types.organization_id


class CreateGroupRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The organization under which the group is to be created.</p>"""
    name: "capo_workmail.types.group_name.GroupName"
    """<p>The name of the group.</p>"""
    hidden_from_global_address_list: "capo_workmail.types.boolean.Boolean"
    """<p>If this parameter is enabled, the group will be hidden from the address book.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGroupRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["Name"] = value["name"]
    out["HiddenFromGlobalAddressList"] = value.get(
        "hidden_from_global_address_list", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGroupRequest:
    out: CreateGroupRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("CreateGroupRequest.organization_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateGroupRequest.name required")
    if "HiddenFromGlobalAddressList" in data:
        out["hidden_from_global_address_list"] = data["HiddenFromGlobalAddressList"]
    else:
        out["hidden_from_global_address_list"] = False
    return out
