"""Generated from Smithy shape ``com.amazonaws.mailmanager#Ipv6Cidrs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ipv6_cidr

Ipv6Cidrs: TypeAlias = list["aws_sdk_mailmanager.types.ipv6_cidr.Ipv6Cidr"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ipv6Cidrs) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Ipv6Cidrs:
    return list(data)
