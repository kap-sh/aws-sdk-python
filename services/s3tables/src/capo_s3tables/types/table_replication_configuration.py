"""Generated from Smithy shape ``com.amazonaws.s3tables#TableReplicationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.iam_role
    import capo_s3tables.types.table_replication_rules


class TableReplicationConfiguration(TypedDict, closed=True):
    role: "capo_s3tables.types.iam_role.IAMRole"
    """<p>The Amazon Resource Name (ARN) of the IAM role that S3 Tables assumes to replicate the table on your behalf.</p>"""
    rules: "capo_s3tables.types.table_replication_rules.TableReplicationRules"
    """<p>An array of replication rules that define where this table should be replicated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableReplicationConfiguration) -> dict:
    out: dict = {}
    out["role"] = value["role"]
    import capo_s3tables.types.table_replication_rules

    out["rules"] = capo_s3tables.types.table_replication_rules.serialize_json(
        value["rules"]
    )
    return out


def deserialize_json(data: dict) -> TableReplicationConfiguration:
    out: TableReplicationConfiguration = {}  # type: ignore[typeddict-item]
    if "role" in data:
        out["role"] = data["role"]
    else:
        raise DeserializationError("TableReplicationConfiguration.role required")
    if "rules" in data:
        import capo_s3tables.types.table_replication_rules

        out["rules"] = capo_s3tables.types.table_replication_rules.deserialize_json(
            data["rules"]
        )
    else:
        raise DeserializationError("TableReplicationConfiguration.rules required")
    return out
