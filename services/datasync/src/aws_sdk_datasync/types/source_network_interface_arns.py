"""Generated from Smithy shape ``com.amazonaws.datasync#SourceNetworkInterfaceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datasync.types.network_interface_arn

SourceNetworkInterfaceArns: TypeAlias = list[
    "aws_sdk_datasync.types.network_interface_arn.NetworkInterfaceArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceNetworkInterfaceArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SourceNetworkInterfaceArns:
    return list(data)
