"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#SelfManageTargetDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.self_manage_target_destination

SelfManageTargetDestinations: TypeAlias = list[
    "capo_migrationhubstrategy.types.self_manage_target_destination.SelfManageTargetDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: SelfManageTargetDestinations) -> list:
    return list(value)


def deserialize_json(data: list) -> SelfManageTargetDestinations:
    return list(data)
