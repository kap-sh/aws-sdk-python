"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteMailboxPermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.organization_id


class DeleteMailboxPermissionsRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier of the organization under which the member (user or group) exists.</p>"""
    entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier of the entity that owns the mailbox.</p> <p>The identifier can be <i>UserId or Group Id</i>, <i>Username or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>"""
    grantee_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier of the entity for which to delete granted permissions.</p> <p>The identifier can be <i>UserId, ResourceID, or Group Id</i>, <i>Username or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Grantee ID: 12345678-1234-1234-1234-123456789012,r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: grantee@domain.tld</p> </li> <li> <p>Grantee name: grantee</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMailboxPermissionsRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["EntityId"] = value["entity_id"]
    out["GranteeId"] = value["grantee_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMailboxPermissionsRequest:
    out: DeleteMailboxPermissionsRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DeleteMailboxPermissionsRequest.organization_id required"
        )
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    else:
        raise DeserializationError("DeleteMailboxPermissionsRequest.entity_id required")
    if "GranteeId" in data:
        out["grantee_id"] = data["GranteeId"]
    else:
        raise DeserializationError(
            "DeleteMailboxPermissionsRequest.grantee_id required"
        )
    return out
