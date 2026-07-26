"""Generated from Smithy shape ``com.amazonaws.rds#DBInstanceAutomatedBackupsReplication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class DBInstanceAutomatedBackupsReplication(TypedDict, closed=True):
    db_instance_automated_backups_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the replicated automated backups.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceAutomatedBackupsReplication,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_instance_automated_backups_arn" in value:
        pairs.append(
            (
                f"{prefix}.DBInstanceAutomatedBackupsArn",
                str(value["db_instance_automated_backups_arn"]),
            )
        )


def deserialize_query(el: Element) -> DBInstanceAutomatedBackupsReplication:
    out: DBInstanceAutomatedBackupsReplication = {}  # type: ignore[typeddict-item]
    child_db_instance_automated_backups_arn = el.find("DBInstanceAutomatedBackupsArn")
    if child_db_instance_automated_backups_arn is not None:
        out["db_instance_automated_backups_arn"] = str(
            child_db_instance_automated_backups_arn.text or ""
        )
    return out
