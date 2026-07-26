"""Generated from Smithy shape ``com.amazonaws.securityhub#VpcInfoCidrBlockSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.vpc_info_cidr_block_set_details

VpcInfoCidrBlockSetList: TypeAlias = list[
    "capo_securityhub.types.vpc_info_cidr_block_set_details.VpcInfoCidrBlockSetDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcInfoCidrBlockSetList) -> list:
    import capo_securityhub.types.vpc_info_cidr_block_set_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.vpc_info_cidr_block_set_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VpcInfoCidrBlockSetList:
    import capo_securityhub.types.vpc_info_cidr_block_set_details

    out: VpcInfoCidrBlockSetList = []
    for item in data:
        out.append(
            capo_securityhub.types.vpc_info_cidr_block_set_details.deserialize_json(
                item
            )
        )
    return out
