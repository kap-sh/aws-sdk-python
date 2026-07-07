"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Contact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.contact_alias
    import aws_sdk_ssm_contacts.types.contact_name
    import aws_sdk_ssm_contacts.types.contact_type
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class Contact(TypedDict, closed=True):
    contact_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact or escalation plan.</p>"""
    alias: "aws_sdk_ssm_contacts.types.contact_alias.ContactAlias"
    """<p>The unique and identifiable alias of the contact or escalation plan.</p>"""
    display_name: NotRequired["aws_sdk_ssm_contacts.types.contact_name.ContactName"]
    """<p>The full name of the contact or escalation plan.</p>"""
    type: "aws_sdk_ssm_contacts.types.contact_type.ContactType"
    """<p>The type of contact.</p> <ul> <li> <p> <code>PERSONAL</code>: A single, individual contact.</p> </li> <li> <p> <code>ESCALATION</code>: An escalation plan.</p> </li> <li> <p> <code>ONCALL_SCHEDULE</code>: An on-call schedule.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Contact) -> dict:
    out: dict = {}
    out["ContactArn"] = value["contact_arn"]
    out["Alias"] = value["alias"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    import aws_sdk_ssm_contacts.types.contact_type

    out["Type"] = aws_sdk_ssm_contacts.types.contact_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Contact:
    out: Contact = {}  # type: ignore[typeddict-item]
    if "ContactArn" in data:
        out["contact_arn"] = data["ContactArn"]
    else:
        raise DeserializationError("Contact.contact_arn required")
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("Contact.alias required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Type" in data:
        import aws_sdk_ssm_contacts.types.contact_type

        out["type"] = aws_sdk_ssm_contacts.types.contact_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("Contact.type required")
    return out
