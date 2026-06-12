"""Generated from Smithy shape ``com.amazonaws.outposts#LifeCycleStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.life_cycle_status

LifeCycleStatusList: TypeAlias = list[
    "aws_sdk_outposts.types.life_cycle_status.LifeCycleStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleStatusList) -> list:
    return list(value)


def deserialize_json(data: list) -> LifeCycleStatusList:
    return list(data)
