"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#TableRestoreStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.table_restore_status

TableRestoreStatusList: TypeAlias = list[
    "aws_sdk_redshift_serverless.types.table_restore_status.TableRestoreStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableRestoreStatusList) -> list:
    import aws_sdk_redshift_serverless.types.table_restore_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_serverless.types.table_restore_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TableRestoreStatusList:
    import aws_sdk_redshift_serverless.types.table_restore_status

    out: TableRestoreStatusList = []
    for item in data:
        out.append(
            aws_sdk_redshift_serverless.types.table_restore_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
