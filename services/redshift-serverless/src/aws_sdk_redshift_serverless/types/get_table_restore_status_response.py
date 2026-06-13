"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetTableRestoreStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.table_restore_status


class GetTableRestoreStatusResponse(TypedDict):
    table_restore_status: NotRequired[
        "aws_sdk_redshift_serverless.types.table_restore_status.TableRestoreStatus"
    ]
    """<p>The returned <code>TableRestoreStatus</code> object that contains information about the status of your <code>RestoreTableFromSnapshot</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableRestoreStatusResponse) -> dict:
    out: dict = {}
    if "table_restore_status" in value:
        import aws_sdk_redshift_serverless.types.table_restore_status

        out["tableRestoreStatus"] = (
            aws_sdk_redshift_serverless.types.table_restore_status.serialize_aws_json_1_1(
                value["table_restore_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableRestoreStatusResponse:
    out: GetTableRestoreStatusResponse = {}  # type: ignore[typeddict-item]
    if "tableRestoreStatus" in data:
        import aws_sdk_redshift_serverless.types.table_restore_status

        out["table_restore_status"] = (
            aws_sdk_redshift_serverless.types.table_restore_status.deserialize_aws_json_1_1(
                data["tableRestoreStatus"]
            )
        )
    return out
