"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.organization_id


class DeleteGroupRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The organization that contains the group.</p>"""
    group_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier of the group to be deleted.</p> <p>The identifier can be the <i>GroupId</i>, or <i>Groupname</i>. The following identity formats are available:</p> <ul> <li> <p>Group ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Group name: group</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGroupRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["GroupId"] = value["group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGroupRequest:
    out: DeleteGroupRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("DeleteGroupRequest.organization_id required")
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("DeleteGroupRequest.group_id required")
    return out
