"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyClusterSnapshotMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string


class ModifyClusterSnapshotMessage(TypedDict):
    snapshot_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the snapshot whose setting you want to modify.</p>"""
    manual_snapshot_retention_period: NotRequired[
        "aws_sdk_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.</p> <p>If the manual snapshot falls outside of the new retention period, you can specify the force option to immediately delete the snapshot.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>"""
    force: NotRequired["aws_sdk_redshift.types.boolean.Boolean"]
    """<p>A Boolean option to override an exception if the retention period has already passed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyClusterSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_identifier" in value:
        pairs.append(
            (f"{prefix}.SnapshotIdentifier", str(value["snapshot_identifier"]))
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


def deserialize_query(el: Element) -> ModifyClusterSnapshotMessage:
    out: ModifyClusterSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_snapshot_identifier = el.find("SnapshotIdentifier")
    if child_snapshot_identifier is not None:
        out["snapshot_identifier"] = str(child_snapshot_identifier.text or "")
    child_manual_snapshot_retention_period = el.find("ManualSnapshotRetentionPeriod")
    if child_manual_snapshot_retention_period is not None:
        out["manual_snapshot_retention_period"] = int(
            child_manual_snapshot_retention_period.text or ""
        )
    child_force = el.find("Force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    return out
