"""Generated from Smithy shape ``com.amazonaws.securityhub#VpcInfoCidrBlockSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.vpc_info_cidr_block_set_details

VpcInfoCidrBlockSetList: TypeAlias = list[
    "aws_sdk_securityhub.types.vpc_info_cidr_block_set_details.VpcInfoCidrBlockSetDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcInfoCidrBlockSetList) -> list:
    import aws_sdk_securityhub.types.vpc_info_cidr_block_set_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.vpc_info_cidr_block_set_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> VpcInfoCidrBlockSetList:
    import aws_sdk_securityhub.types.vpc_info_cidr_block_set_details

    out: VpcInfoCidrBlockSetList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.vpc_info_cidr_block_set_details.deserialize_json(
                item
            )
        )
    return out
