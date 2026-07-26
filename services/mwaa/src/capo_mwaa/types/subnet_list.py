"""Generated from Smithy shape ``com.amazonaws.mwaa#SubnetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa.types.subnet_id

SubnetList: TypeAlias = list["capo_mwaa.types.subnet_id.SubnetId"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetList:
    return list(data)
