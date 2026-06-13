"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ReplicationStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.replication_status

ReplicationStatuses: TypeAlias = list[
    "aws_sdk_gameliftstreams.types.replication_status.ReplicationStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStatuses) -> list:
    import aws_sdk_gameliftstreams.types.replication_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gameliftstreams.types.replication_status.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReplicationStatuses:
    import aws_sdk_gameliftstreams.types.replication_status

    out: ReplicationStatuses = []
    for item in data:
        out.append(
            aws_sdk_gameliftstreams.types.replication_status.deserialize_json(item)
        )
    return out
