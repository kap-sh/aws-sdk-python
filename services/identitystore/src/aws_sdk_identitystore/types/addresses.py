"""Generated from Smithy shape ``com.amazonaws.identitystore#Addresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.address

Addresses: TypeAlias = list["aws_sdk_identitystore.types.address.Address"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Addresses) -> list:
    import aws_sdk_identitystore.types.address

    out: list = []
    for item in value:
        out.append(aws_sdk_identitystore.types.address.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Addresses:
    import aws_sdk_identitystore.types.address

    out: Addresses = []
    for item in data:
        out.append(aws_sdk_identitystore.types.address.deserialize_aws_json_1_1(item))
    return out
