"""Generated from Smithy shape ``com.amazonaws.s3tables#ReplicationDestinationStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.replication_destination_status_model

ReplicationDestinationStatuses: TypeAlias = list[
    "aws_sdk_s3tables.types.replication_destination_status_model.ReplicationDestinationStatusModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationDestinationStatuses) -> list:
    import aws_sdk_s3tables.types.replication_destination_status_model

    out: list = []
    for item in value:
        out.append(
            aws_sdk_s3tables.types.replication_destination_status_model.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ReplicationDestinationStatuses:
    import aws_sdk_s3tables.types.replication_destination_status_model

    out: ReplicationDestinationStatuses = []
    for item in data:
        out.append(
            aws_sdk_s3tables.types.replication_destination_status_model.deserialize_json(
                item
            )
        )
    return out
