"""Generated from Smithy shape ``com.amazonaws.workmail#AssociateMemberToGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.organization_id


class AssociateMemberToGroupRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The organization under which the group exists.</p>"""
    group_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The group to which the member (user or group) is associated.</p> <p>The identifier can accept <i>GroupId</i>, <i>Groupname</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Group ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: group@domain.tld</p> </li> <li> <p>Group name: group</p> </li> </ul>"""
    member_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The member (user or group) to associate to the group.</p> <p>The member ID can accept <i>UserID or GroupId</i>, <i>Username or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Member: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: member@domain.tld</p> </li> <li> <p>Member name: member</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateMemberToGroupRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["GroupId"] = value["group_id"]
    out["MemberId"] = value["member_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateMemberToGroupRequest:
    out: AssociateMemberToGroupRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "AssociateMemberToGroupRequest.organization_id required"
        )
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("AssociateMemberToGroupRequest.group_id required")
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    else:
        raise DeserializationError("AssociateMemberToGroupRequest.member_id required")
    return out
