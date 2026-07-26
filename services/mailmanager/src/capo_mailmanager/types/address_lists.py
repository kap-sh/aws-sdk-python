"""Generated from Smithy shape ``com.amazonaws.mailmanager#AddressLists``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.address_list

AddressLists: TypeAlias = list["capo_mailmanager.types.address_list.AddressList"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddressLists) -> list:
    import capo_mailmanager.types.address_list

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.address_list.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AddressLists:
    import capo_mailmanager.types.address_list

    out: AddressLists = []
    for item in data:
        out.append(capo_mailmanager.types.address_list.deserialize_aws_json_1_0(item))
    return out
