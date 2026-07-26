"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#LogExportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_serverless.types.log_export

LogExportList: TypeAlias = list["capo_redshift_serverless.types.log_export.LogExport"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogExportList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LogExportList:
    return list(data)
