"""Generated from Smithy shape ``com.amazonaws.invoicing#Contacts``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_invoicing.types.contact

Contacts: TypeAlias = list["aws_sdk_invoicing.types.contact.Contact"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Contacts) -> list:
    import aws_sdk_invoicing.types.contact
    out: list = []
    for item in value:
        out.append(aws_sdk_invoicing.types.contact.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Contacts:
    import aws_sdk_invoicing.types.contact
    out: Contacts = []
    for item in data:
        out.append(aws_sdk_invoicing.types.contact.deserialize_aws_json_1_0(item))
    return out