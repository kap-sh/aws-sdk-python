"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceDataReplicationInitiationSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.recovery_instance_data_replication_initiation_step

RecoveryInstanceDataReplicationInitiationSteps: TypeAlias = list[
    "aws_sdk_drs.types.recovery_instance_data_replication_initiation_step.RecoveryInstanceDataReplicationInitiationStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceDataReplicationInitiationSteps) -> list:
    import aws_sdk_drs.types.recovery_instance_data_replication_initiation_step

    out: list = []
    for item in value:
        out.append(
            aws_sdk_drs.types.recovery_instance_data_replication_initiation_step.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecoveryInstanceDataReplicationInitiationSteps:
    import aws_sdk_drs.types.recovery_instance_data_replication_initiation_step

    out: RecoveryInstanceDataReplicationInitiationSteps = []
    for item in data:
        out.append(
            aws_sdk_drs.types.recovery_instance_data_replication_initiation_step.deserialize_json(
                item
            )
        )
    return out
