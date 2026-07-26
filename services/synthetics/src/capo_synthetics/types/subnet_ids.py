"""Generated from Smithy shape ``com.amazonaws.synthetics#SubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.subnet_id

SubnetIds: TypeAlias = list["capo_synthetics.types.subnet_id.SubnetId"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetIds:
    return list(data)
