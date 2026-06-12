"""Generated from Smithy shape ``com.amazonaws.securityhub#VpcInfoIpv6CidrBlockSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.vpc_info_ipv6_cidr_block_set_details

VpcInfoIpv6CidrBlockSetList: TypeAlias = list[
    "aws_sdk_securityhub.types.vpc_info_ipv6_cidr_block_set_details.VpcInfoIpv6CidrBlockSetDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcInfoIpv6CidrBlockSetList) -> list:
    import aws_sdk_securityhub.types.vpc_info_ipv6_cidr_block_set_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.vpc_info_ipv6_cidr_block_set_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> VpcInfoIpv6CidrBlockSetList:
    import aws_sdk_securityhub.types.vpc_info_ipv6_cidr_block_set_details

    out: VpcInfoIpv6CidrBlockSetList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.vpc_info_ipv6_cidr_block_set_details.deserialize_json(
                item
            )
        )
    return out
