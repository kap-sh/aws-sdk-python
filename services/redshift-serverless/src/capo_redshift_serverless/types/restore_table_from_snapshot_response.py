"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RestoreTableFromSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.table_restore_status


class RestoreTableFromSnapshotResponse(TypedDict, closed=True):
    table_restore_status: NotRequired[
        "capo_redshift_serverless.types.table_restore_status.TableRestoreStatus"
    ]
    """<p>The TableRestoreStatus object that contains the status of the restore operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreTableFromSnapshotResponse) -> dict:
    out: dict = {}
    if "table_restore_status" in value:
        import capo_redshift_serverless.types.table_restore_status

        out["tableRestoreStatus"] = (
            capo_redshift_serverless.types.table_restore_status.serialize_aws_json_1_1(
                value["table_restore_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreTableFromSnapshotResponse:
    out: RestoreTableFromSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "tableRestoreStatus" in data:
        import capo_redshift_serverless.types.table_restore_status

        out["table_restore_status"] = (
            capo_redshift_serverless.types.table_restore_status.deserialize_aws_json_1_1(
                data["tableRestoreStatus"]
            )
        )
    return out
