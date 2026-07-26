"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Contacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.contact

Contacts: TypeAlias = list["capo_partnercentral_benefits.types.contact.Contact"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Contacts) -> list:
    import capo_partnercentral_benefits.types.contact

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_benefits.types.contact.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Contacts:
    import capo_partnercentral_benefits.types.contact

    out: Contacts = []
    for item in data:
        out.append(
            capo_partnercentral_benefits.types.contact.deserialize_aws_json_1_0(item)
        )
    return out
