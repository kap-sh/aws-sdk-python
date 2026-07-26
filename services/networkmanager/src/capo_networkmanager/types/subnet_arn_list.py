"""Generated from Smithy shape ``com.amazonaws.networkmanager#SubnetArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.subnet_arn

SubnetArnList: TypeAlias = list["capo_networkmanager.types.subnet_arn.SubnetArn"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetArnList:
    return list(data)
