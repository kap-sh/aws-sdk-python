"""Generated from Smithy shape ``com.amazonaws.odb#CustomerContacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.customer_contact

CustomerContacts: TypeAlias = list["capo_odb.types.customer_contact.CustomerContact"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomerContacts) -> list:
    import capo_odb.types.customer_contact

    out: list = []
    for item in value:
        out.append(capo_odb.types.customer_contact.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> CustomerContacts:
    import capo_odb.types.customer_contact

    out: CustomerContacts = []
    for item in data:
        out.append(capo_odb.types.customer_contact.deserialize_aws_json_1_0(item))
    return out
