"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineDriftStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.enabled_baseline_drift_status

EnabledBaselineDriftStatuses: TypeAlias = list[
    "capo_controltower.types.enabled_baseline_drift_status.EnabledBaselineDriftStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineDriftStatuses) -> list:
    import capo_controltower.types.enabled_baseline_drift_status

    out: list = []
    for item in value:
        out.append(
            capo_controltower.types.enabled_baseline_drift_status.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EnabledBaselineDriftStatuses:
    import capo_controltower.types.enabled_baseline_drift_status

    out: EnabledBaselineDriftStatuses = []
    for item in data:
        out.append(
            capo_controltower.types.enabled_baseline_drift_status.deserialize_json(item)
        )
    return out
