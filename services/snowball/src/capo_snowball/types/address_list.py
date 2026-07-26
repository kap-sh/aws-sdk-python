"""Generated from Smithy shape ``com.amazonaws.snowball#AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.address

AddressList: TypeAlias = list["capo_snowball.types.address.Address"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddressList) -> list:
    import capo_snowball.types.address

    out: list = []
    for item in value:
        out.append(capo_snowball.types.address.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AddressList:
    import capo_snowball.types.address

    out: AddressList = []
    for item in data:
        out.append(capo_snowball.types.address.deserialize_aws_json_1_1(item))
    return out
