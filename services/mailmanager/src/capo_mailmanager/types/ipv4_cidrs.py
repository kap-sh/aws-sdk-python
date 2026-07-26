"""Generated from Smithy shape ``com.amazonaws.mailmanager#Ipv4Cidrs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.ipv4_cidr

Ipv4Cidrs: TypeAlias = list["capo_mailmanager.types.ipv4_cidr.Ipv4Cidr"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ipv4Cidrs) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Ipv4Cidrs:
    return list(data)
