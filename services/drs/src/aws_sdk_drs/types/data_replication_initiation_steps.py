"""Generated from Smithy shape ``com.amazonaws.drs#DataReplicationInitiationSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.data_replication_initiation_step

DataReplicationInitiationSteps: TypeAlias = list[
    "aws_sdk_drs.types.data_replication_initiation_step.DataReplicationInitiationStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationInitiationSteps) -> list:
    import aws_sdk_drs.types.data_replication_initiation_step

    out: list = []
    for item in value:
        out.append(
            aws_sdk_drs.types.data_replication_initiation_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataReplicationInitiationSteps:
    import aws_sdk_drs.types.data_replication_initiation_step

    out: DataReplicationInitiationSteps = []
    for item in data:
        out.append(
            aws_sdk_drs.types.data_replication_initiation_step.deserialize_json(item)
        )
    return out
