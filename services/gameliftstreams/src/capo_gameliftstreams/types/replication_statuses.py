"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ReplicationStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gameliftstreams.types.replication_status

ReplicationStatuses: TypeAlias = list[
    "capo_gameliftstreams.types.replication_status.ReplicationStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStatuses) -> list:
    import capo_gameliftstreams.types.replication_status

    out: list = []
    for item in value:
        out.append(capo_gameliftstreams.types.replication_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReplicationStatuses:
    import capo_gameliftstreams.types.replication_status

    out: ReplicationStatuses = []
    for item in data:
        out.append(capo_gameliftstreams.types.replication_status.deserialize_json(item))
    return out
