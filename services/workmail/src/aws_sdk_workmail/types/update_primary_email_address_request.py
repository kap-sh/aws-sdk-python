"""Generated from Smithy shape ``com.amazonaws.workmail#UpdatePrimaryEmailAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.email_address
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.organization_id


class UpdatePrimaryEmailAddressRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The organization that contains the user, group, or resource to update.</p>"""
    entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The user, group, or resource to update.</p> <p>The identifier can accept <i>UseriD, ResourceId, or GroupId</i>, <i>Username, Resourcename, or Groupname</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>"""
    email: "aws_sdk_workmail.types.email_address.EmailAddress"
    """<p>The value of the email to be updated as primary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePrimaryEmailAddressRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["EntityId"] = value["entity_id"]
    out["Email"] = value["email"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePrimaryEmailAddressRequest:
    out: UpdatePrimaryEmailAddressRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "UpdatePrimaryEmailAddressRequest.organization_id required"
        )
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    else:
        raise DeserializationError(
            "UpdatePrimaryEmailAddressRequest.entity_id required"
        )
    if "Email" in data:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("UpdatePrimaryEmailAddressRequest.email required")
    return out
