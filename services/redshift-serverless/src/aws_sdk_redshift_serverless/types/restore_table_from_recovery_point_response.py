"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RestoreTableFromRecoveryPointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.table_restore_status


class RestoreTableFromRecoveryPointResponse(TypedDict):
    table_restore_status: NotRequired[
        "aws_sdk_redshift_serverless.types.table_restore_status.TableRestoreStatus"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreTableFromRecoveryPointResponse) -> dict:
    out: dict = {}
    if "table_restore_status" in value:
        import aws_sdk_redshift_serverless.types.table_restore_status

        out["tableRestoreStatus"] = (
            aws_sdk_redshift_serverless.types.table_restore_status.serialize_aws_json_1_1(
                value["table_restore_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreTableFromRecoveryPointResponse:
    out: RestoreTableFromRecoveryPointResponse = {}  # type: ignore[typeddict-item]
    if "tableRestoreStatus" in data:
        import aws_sdk_redshift_serverless.types.table_restore_status

        out["table_restore_status"] = (
            aws_sdk_redshift_serverless.types.table_restore_status.deserialize_aws_json_1_1(
                data["tableRestoreStatus"]
            )
        )
    return out
