"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceDataReplicationInitiationSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_instance_data_replication_initiation_step

RecoveryInstanceDataReplicationInitiationSteps: TypeAlias = list[
    "capo_drs.types.recovery_instance_data_replication_initiation_step.RecoveryInstanceDataReplicationInitiationStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceDataReplicationInitiationSteps) -> list:
    import capo_drs.types.recovery_instance_data_replication_initiation_step

    out: list = []
    for item in value:
        out.append(
            capo_drs.types.recovery_instance_data_replication_initiation_step.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecoveryInstanceDataReplicationInitiationSteps:
    import capo_drs.types.recovery_instance_data_replication_initiation_step

    out: RecoveryInstanceDataReplicationInitiationSteps = []
    for item in data:
        out.append(
            capo_drs.types.recovery_instance_data_replication_initiation_step.deserialize_json(
                item
            )
        )
    return out
