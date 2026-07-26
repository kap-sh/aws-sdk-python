"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#NoPreferenceTargetDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.no_preference_target_destination

NoPreferenceTargetDestinations: TypeAlias = list[
    "capo_migrationhubstrategy.types.no_preference_target_destination.NoPreferenceTargetDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: NoPreferenceTargetDestinations) -> list:
    return list(value)


def deserialize_json(data: list) -> NoPreferenceTargetDestinations:
    return list(data)
