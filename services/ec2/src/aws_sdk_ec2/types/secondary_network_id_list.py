"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryNetworkIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_network_id

SecondaryNetworkIdList: TypeAlias = list[
    "aws_sdk_ec2.types.secondary_network_id.SecondaryNetworkId"
]
