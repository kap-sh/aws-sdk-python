"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetContactResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.contact_alias
    import aws_sdk_ssm_contacts.types.contact_name
    import aws_sdk_ssm_contacts.types.contact_type
    import aws_sdk_ssm_contacts.types.plan
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class GetContactResult(TypedDict):
    contact_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the contact or escalation plan.</p>"""
    alias: "aws_sdk_ssm_contacts.types.contact_alias.ContactAlias"
    """<p>The alias of the contact or escalation plan. The alias is unique and identifiable.</p>"""
    display_name: NotRequired["aws_sdk_ssm_contacts.types.contact_name.ContactName"]
    """<p>The full name of the contact or escalation plan.</p>"""
    type: "aws_sdk_ssm_contacts.types.contact_type.ContactType"
    """<p>The type of contact.</p>"""
    plan: "aws_sdk_ssm_contacts.types.plan.Plan"
    """<p>Details about the specific timing or stages and targets of the escalation plan or engagement plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContactResult) -> dict:
    out: dict = {}
    out["ContactArn"] = value["contact_arn"]
    out["Alias"] = value["alias"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    import aws_sdk_ssm_contacts.types.contact_type

    out["Type"] = aws_sdk_ssm_contacts.types.contact_type.serialize_aws_json_1_1(
        value["type"]
    )
    import aws_sdk_ssm_contacts.types.plan

    out["Plan"] = aws_sdk_ssm_contacts.types.plan.serialize_aws_json_1_1(value["plan"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContactResult:
    out: GetContactResult = {}  # type: ignore[typeddict-item]
    if "ContactArn" in data:
        out["contact_arn"] = data["ContactArn"]
    else:
        raise DeserializationError("GetContactResult.contact_arn required")
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("GetContactResult.alias required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Type" in data:
        import aws_sdk_ssm_contacts.types.contact_type

        out["type"] = aws_sdk_ssm_contacts.types.contact_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("GetContactResult.type required")
    if "Plan" in data:
        import aws_sdk_ssm_contacts.types.plan

        out["plan"] = aws_sdk_ssm_contacts.types.plan.deserialize_aws_json_1_1(
            data["Plan"]
        )
    else:
        raise DeserializationError("GetContactResult.plan required")
    return out
