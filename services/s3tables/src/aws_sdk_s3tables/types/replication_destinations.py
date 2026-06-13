"""Generated from Smithy shape ``com.amazonaws.s3tables#ReplicationDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.replication_destination

ReplicationDestinations: TypeAlias = list[
    "aws_sdk_s3tables.types.replication_destination.ReplicationDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationDestinations) -> list:
    import aws_sdk_s3tables.types.replication_destination

    out: list = []
    for item in value:
        out.append(aws_sdk_s3tables.types.replication_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReplicationDestinations:
    import aws_sdk_s3tables.types.replication_destination

    out: ReplicationDestinations = []
    for item in data:
        out.append(
            aws_sdk_s3tables.types.replication_destination.deserialize_json(item)
        )
    return out
