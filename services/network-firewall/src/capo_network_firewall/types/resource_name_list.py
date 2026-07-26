"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ResourceNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_name

ResourceNameList: TypeAlias = list[
    "capo_network_firewall.types.resource_name.ResourceName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ResourceNameList:
    return list(data)
