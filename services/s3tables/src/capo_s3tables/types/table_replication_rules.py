"""Generated from Smithy shape ``com.amazonaws.s3tables#TableReplicationRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3tables.types.table_replication_rule

TableReplicationRules: TypeAlias = list[
    "capo_s3tables.types.table_replication_rule.TableReplicationRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: TableReplicationRules) -> list:
    import capo_s3tables.types.table_replication_rule

    out: list = []
    for item in value:
        out.append(capo_s3tables.types.table_replication_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> TableReplicationRules:
    import capo_s3tables.types.table_replication_rule

    out: TableReplicationRules = []
    for item in data:
        out.append(capo_s3tables.types.table_replication_rule.deserialize_json(item))
    return out
