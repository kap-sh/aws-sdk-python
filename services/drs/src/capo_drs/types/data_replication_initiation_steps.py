"""Generated from Smithy shape ``com.amazonaws.drs#DataReplicationInitiationSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.data_replication_initiation_step

DataReplicationInitiationSteps: TypeAlias = list[
    "capo_drs.types.data_replication_initiation_step.DataReplicationInitiationStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationInitiationSteps) -> list:
    import capo_drs.types.data_replication_initiation_step

    out: list = []
    for item in value:
        out.append(capo_drs.types.data_replication_initiation_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataReplicationInitiationSteps:
    import capo_drs.types.data_replication_initiation_step

    out: DataReplicationInitiationSteps = []
    for item in data:
        out.append(
            capo_drs.types.data_replication_initiation_step.deserialize_json(item)
        )
    return out
