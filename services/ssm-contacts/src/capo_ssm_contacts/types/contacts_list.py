"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ContactsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_contacts.types.contact

ContactsList: TypeAlias = list["capo_ssm_contacts.types.contact.Contact"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactsList) -> list:
    import capo_ssm_contacts.types.contact

    out: list = []
    for item in value:
        out.append(capo_ssm_contacts.types.contact.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContactsList:
    import capo_ssm_contacts.types.contact

    out: ContactsList = []
    for item in data:
        out.append(capo_ssm_contacts.types.contact.deserialize_aws_json_1_1(item))
    return out
