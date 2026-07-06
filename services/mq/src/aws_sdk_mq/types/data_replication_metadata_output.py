"""Generated from Smithy shape ``com.amazonaws.mq#DataReplicationMetadataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.data_replication_counterpart


class DataReplicationMetadataOutput(TypedDict, closed=True):
    data_replication_counterpart: NotRequired[
        "aws_sdk_mq.types.data_replication_counterpart.DataReplicationCounterpart"
    ]
    """<p>Describes the replica/primary broker. Only returned if this broker is currently set as a primary or replica in the broker's dataReplicationRole property.</p>"""
    data_replication_role: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Defines the role of this broker in a data replication pair. When a replica broker is promoted to primary, this role is interchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationMetadataOutput) -> dict:
    out: dict = {}
    if "data_replication_counterpart" in value:
        import aws_sdk_mq.types.data_replication_counterpart

        out["dataReplicationCounterpart"] = (
            aws_sdk_mq.types.data_replication_counterpart.serialize_json(
                value["data_replication_counterpart"]
            )
        )
    if "data_replication_role" in value:
        out["dataReplicationRole"] = value["data_replication_role"]
    return out


def deserialize_json(data: dict) -> DataReplicationMetadataOutput:
    out: DataReplicationMetadataOutput = {}  # type: ignore[typeddict-item]
    if "dataReplicationCounterpart" in data:
        import aws_sdk_mq.types.data_replication_counterpart

        out["data_replication_counterpart"] = (
            aws_sdk_mq.types.data_replication_counterpart.deserialize_json(
                data["dataReplicationCounterpart"]
            )
        )
    if "dataReplicationRole" in data:
        out["data_replication_role"] = data["dataReplicationRole"]
    return out
