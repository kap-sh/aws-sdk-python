"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CreateContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.contact_alias
    import aws_sdk_ssm_contacts.types.contact_name
    import aws_sdk_ssm_contacts.types.contact_type
    import aws_sdk_ssm_contacts.types.idempotency_token
    import aws_sdk_ssm_contacts.types.plan
    import aws_sdk_ssm_contacts.types.tags_list


class CreateContactRequest(TypedDict, closed=True):
    alias: "aws_sdk_ssm_contacts.types.contact_alias.ContactAlias"
    """<p>The short name to quickly identify a contact or escalation plan. The contact alias must be unique and identifiable.</p>"""
    display_name: NotRequired["aws_sdk_ssm_contacts.types.contact_name.ContactName"]
    """<p>The full name of the contact or escalation plan.</p>"""
    type: "aws_sdk_ssm_contacts.types.contact_type.ContactType"
    """<p>The type of contact to create.</p> <ul> <li> <p> <code>PERSONAL</code>: A single, individual contact.</p> </li> <li> <p> <code>ESCALATION</code>: An escalation plan.</p> </li> <li> <p> <code>ONCALL_SCHEDULE</code>: An on-call schedule.</p> </li> </ul>"""
    plan: "aws_sdk_ssm_contacts.types.plan.Plan"
    """<p>A list of stages. A contact has an engagement plan with stages that contact specified contact channels. An escalation plan uses stages that contact specified contacts.</p>"""
    tags: NotRequired["aws_sdk_ssm_contacts.types.tags_list.TagsList"]
    """<p>Adds a tag to the target. You can only tag resources created in the first Region of your replication set.</p>"""
    idempotency_token: NotRequired[
        "aws_sdk_ssm_contacts.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A token ensuring that the operation is called only once with the specified details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContactRequest) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    import aws_sdk_ssm_contacts.types.contact_type

    out["Type"] = aws_sdk_ssm_contacts.types.contact_type.serialize_aws_json_1_1(
        value["type"]
    )
    import aws_sdk_ssm_contacts.types.plan

    out["Plan"] = aws_sdk_ssm_contacts.types.plan.serialize_aws_json_1_1(value["plan"])
    if "tags" in value:
        import aws_sdk_ssm_contacts.types.tags_list

        out["Tags"] = aws_sdk_ssm_contacts.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContactRequest:
    out: CreateContactRequest = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("CreateContactRequest.alias required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Type" in data:
        import aws_sdk_ssm_contacts.types.contact_type

        out["type"] = aws_sdk_ssm_contacts.types.contact_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateContactRequest.type required")
    if "Plan" in data:
        import aws_sdk_ssm_contacts.types.plan

        out["plan"] = aws_sdk_ssm_contacts.types.plan.deserialize_aws_json_1_1(
            data["Plan"]
        )
    else:
        raise DeserializationError("CreateContactRequest.plan required")
    if "Tags" in data:
        import aws_sdk_ssm_contacts.types.tags_list

        out["tags"] = aws_sdk_ssm_contacts.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
