"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineEnablementStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.enablement_status

EnabledBaselineEnablementStatuses: TypeAlias = list[
    "capo_controltower.types.enablement_status.EnablementStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineEnablementStatuses) -> list:
    import capo_controltower.types.enablement_status

    out: list = []
    for item in value:
        out.append(capo_controltower.types.enablement_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnabledBaselineEnablementStatuses:
    import capo_controltower.types.enablement_status

    out: EnabledBaselineEnablementStatuses = []
    for item in data:
        out.append(capo_controltower.types.enablement_status.deserialize_json(item))
    return out
