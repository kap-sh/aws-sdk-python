"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#IpAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.ip_address

IpAddresses: TypeAlias = list["capo_global_accelerator.types.ip_address.IpAddress"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddresses) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IpAddresses:
    return list(data)
