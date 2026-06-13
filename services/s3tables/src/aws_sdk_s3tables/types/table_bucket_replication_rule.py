"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketReplicationRule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.replication_destinations


class TableBucketReplicationRule(TypedDict):
    destinations: (
        "aws_sdk_s3tables.types.replication_destinations.ReplicationDestinations"
    )
    """<p>An array of destination table buckets where tables should be replicated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableBucketReplicationRule) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.replication_destinations

    out["destinations"] = (
        aws_sdk_s3tables.types.replication_destinations.serialize_json(
            value["destinations"]
        )
    )
    return out


def deserialize_json(data: dict) -> TableBucketReplicationRule:
    out: TableBucketReplicationRule = {}  # type: ignore[typeddict-item]
    if "destinations" in data:
        import aws_sdk_s3tables.types.replication_destinations

        out["destinations"] = (
            aws_sdk_s3tables.types.replication_destinations.deserialize_json(
                data["destinations"]
            )
        )
    else:
        raise DeserializationError("TableBucketReplicationRule.destinations required")
    return out
