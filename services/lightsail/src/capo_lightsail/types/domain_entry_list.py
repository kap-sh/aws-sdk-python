"""Generated from Smithy shape ``com.amazonaws.lightsail#DomainEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.domain_entry

DomainEntryList: TypeAlias = list["capo_lightsail.types.domain_entry.DomainEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainEntryList) -> list:
    import capo_lightsail.types.domain_entry

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.domain_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DomainEntryList:
    import capo_lightsail.types.domain_entry

    out: DomainEntryList = []
    for item in data:
        out.append(capo_lightsail.types.domain_entry.deserialize_aws_json_1_1(item))
    return out
