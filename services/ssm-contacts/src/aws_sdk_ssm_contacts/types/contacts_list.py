"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ContactsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.contact

ContactsList: TypeAlias = list["aws_sdk_ssm_contacts.types.contact.Contact"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactsList) -> list:
    import aws_sdk_ssm_contacts.types.contact

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_contacts.types.contact.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContactsList:
    import aws_sdk_ssm_contacts.types.contact

    out: ContactsList = []
    for item in data:
        out.append(aws_sdk_ssm_contacts.types.contact.deserialize_aws_json_1_1(item))
    return out
