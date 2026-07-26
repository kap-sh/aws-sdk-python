"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ResourceArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn

ResourceArnList: TypeAlias = list[
    "capo_network_firewall.types.resource_arn.ResourceArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceArnList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ResourceArnList:
    return list(data)
