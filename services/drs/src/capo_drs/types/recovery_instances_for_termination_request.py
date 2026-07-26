"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstancesForTerminationRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_instance_id

RecoveryInstancesForTerminationRequest: TypeAlias = list[
    "capo_drs.types.recovery_instance_id.RecoveryInstanceID"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstancesForTerminationRequest) -> list:
    return list(value)


def deserialize_json(data: list) -> RecoveryInstancesForTerminationRequest:
    return list(data)
