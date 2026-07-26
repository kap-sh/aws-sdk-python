"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketReplicationRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3tables.types.table_bucket_replication_rule

TableBucketReplicationRules: TypeAlias = list[
    "capo_s3tables.types.table_bucket_replication_rule.TableBucketReplicationRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: TableBucketReplicationRules) -> list:
    import capo_s3tables.types.table_bucket_replication_rule

    out: list = []
    for item in value:
        out.append(
            capo_s3tables.types.table_bucket_replication_rule.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TableBucketReplicationRules:
    import capo_s3tables.types.table_bucket_replication_rule

    out: TableBucketReplicationRules = []
    for item in data:
        out.append(
            capo_s3tables.types.table_bucket_replication_rule.deserialize_json(item)
        )
    return out
