"""Generated from Smithy shape ``com.amazonaws.rds#StopDBInstanceAutomatedBackupsReplicationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class StopDBInstanceAutomatedBackupsReplicationMessage(TypedDict, closed=True):
    source_db_instance_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the source DB instance for which to stop replicating automate backups, for example, <code>arn:aws:rds:us-west-2:123456789012:db:mydatabase</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StopDBInstanceAutomatedBackupsReplicationMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "source_db_instance_arn" in value:
        pairs.append(
            (f"{prefix}.SourceDBInstanceArn", str(value["source_db_instance_arn"]))
        )


def deserialize_query(el: Element) -> StopDBInstanceAutomatedBackupsReplicationMessage:
    out: StopDBInstanceAutomatedBackupsReplicationMessage = {}  # type: ignore[typeddict-item]
    child_source_db_instance_arn = el.find("SourceDBInstanceArn")
    if child_source_db_instance_arn is not None:
        out["source_db_instance_arn"] = str(child_source_db_instance_arn.text or "")
    return out
