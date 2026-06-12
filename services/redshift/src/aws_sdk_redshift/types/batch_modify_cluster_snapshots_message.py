"""Generated from Smithy shape ``com.amazonaws.redshift#BatchModifyClusterSnapshotsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.snapshot_identifier_list


class BatchModifyClusterSnapshotsMessage(TypedDict):
    snapshot_identifier_list: NotRequired[
        "aws_sdk_redshift.types.snapshot_identifier_list.SnapshotIdentifierList"
    ]
    """<p>A list of snapshot identifiers you want to modify.</p>"""
    manual_snapshot_retention_period: NotRequired[
        "aws_sdk_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days that a manual snapshot is retained. If you specify the value -1, the manual snapshot is retained indefinitely.</p> <p>The number must be either -1 or an integer between 1 and 3,653.</p> <p>If you decrease the manual snapshot retention period from its current value, existing manual snapshots that fall outside of the new retention period will return an error. If you want to suppress the errors and delete the snapshots, use the force option. </p>"""
    force: NotRequired["aws_sdk_redshift.types.boolean.Boolean"]
    """<p>A boolean value indicating whether to override an exception if the retention period has passed. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchModifyClusterSnapshotsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_identifier_list" in value:
        import aws_sdk_redshift.types.snapshot_identifier_list

        aws_sdk_redshift.types.snapshot_identifier_list.serialize_query(
            value["snapshot_identifier_list"], pairs, f"{prefix}.SnapshotIdentifierList"
        )
    if "manual_snapshot_retention_period" in value:
        pairs.append(
            (
                f"{prefix}.ManualSnapshotRetentionPeriod",
                str(value["manual_snapshot_retention_period"]),
            )
        )
    if "force" in value:
        pairs.append((f"{prefix}.Force", "true" if value["force"] else "false"))


def deserialize_query(el: Element) -> BatchModifyClusterSnapshotsMessage:
    out: BatchModifyClusterSnapshotsMessage = {}  # type: ignore[typeddict-item]
    child_snapshot_identifier_list = el.find("SnapshotIdentifierList")
    if child_snapshot_identifier_list is not None:
        import aws_sdk_redshift.types.snapshot_identifier_list

        out["snapshot_identifier_list"] = (
            aws_sdk_redshift.types.snapshot_identifier_list.deserialize_query(
                child_snapshot_identifier_list
            )
        )
    child_manual_snapshot_retention_period = el.find("ManualSnapshotRetentionPeriod")
    if child_manual_snapshot_retention_period is not None:
        out["manual_snapshot_retention_period"] = int(
            child_manual_snapshot_retention_period.text or ""
        )
    child_force = el.find("Force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    return out
