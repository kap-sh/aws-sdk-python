"""Generated from Smithy shape ``com.amazonaws.s3tables#ReplicationDestinationStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3tables.types.replication_destination_status_model

ReplicationDestinationStatuses: TypeAlias = list[
    "capo_s3tables.types.replication_destination_status_model.ReplicationDestinationStatusModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationDestinationStatuses) -> list:
    import capo_s3tables.types.replication_destination_status_model

    out: list = []
    for item in value:
        out.append(
            capo_s3tables.types.replication_destination_status_model.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ReplicationDestinationStatuses:
    import capo_s3tables.types.replication_destination_status_model

    out: ReplicationDestinationStatuses = []
    for item in data:
        out.append(
            capo_s3tables.types.replication_destination_status_model.deserialize_json(
                item
            )
        )
    return out
