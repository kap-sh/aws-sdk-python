"""Generated from Smithy shape ``com.amazonaws.workmail#RegisterToWorkMailRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.email_address
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.organization_id


class RegisterToWorkMailRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization under which the user, group, or resource exists.</p>"""
    entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier for the user, group, or resource to be updated.</p> <p>The identifier can accept <i>UserId, ResourceId, or GroupId</i>, or <i>Username, Resourcename, or Groupname</i>. The following identity formats are available:</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Entity name: entity</p> </li> </ul>"""
    email: "aws_sdk_workmail.types.email_address.EmailAddress"
    """<p>The email for the user, group, or resource to be updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterToWorkMailRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["EntityId"] = value["entity_id"]
    out["Email"] = value["email"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterToWorkMailRequest:
    out: RegisterToWorkMailRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("RegisterToWorkMailRequest.organization_id required")
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    else:
        raise DeserializationError("RegisterToWorkMailRequest.entity_id required")
    if "Email" in data:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("RegisterToWorkMailRequest.email required")
    return out
