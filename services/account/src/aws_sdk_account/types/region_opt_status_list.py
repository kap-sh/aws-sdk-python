"""Generated from Smithy shape ``com.amazonaws.account#RegionOptStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_account.types.region_opt_status

RegionOptStatusList: TypeAlias = list[
    "aws_sdk_account.types.region_opt_status.RegionOptStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegionOptStatusList) -> list:
    return list(value)


def deserialize_json(data: list) -> RegionOptStatusList:
    return list(data)
