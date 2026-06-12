"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#StartImportFileTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migrationhubstrategy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.data_source_type
    import aws_sdk_migrationhubstrategy.types.group_ids
    import aws_sdk_migrationhubstrategy.types.import_s3_bucket
    import aws_sdk_migrationhubstrategy.types.string


class StartImportFileTaskRequest(TypedDict):
    name: "aws_sdk_migrationhubstrategy.types.string.String"
    """<p> A descriptive name for the request. </p>"""
    s3_bucket: "aws_sdk_migrationhubstrategy.types.import_s3_bucket.importS3Bucket"
    """<p> The S3 bucket where the import file is located. The bucket name is required to begin with <code>migrationhub-strategy-</code>.</p>"""
    s3key: "aws_sdk_migrationhubstrategy.types.string.String"
    """<p> The Amazon S3 key name of the import file. </p>"""
    data_source_type: NotRequired[
        "aws_sdk_migrationhubstrategy.types.data_source_type.DataSourceType"
    ]
    """<p>Specifies the source that the servers are coming from. By default, Strategy Recommendations assumes that the servers specified in the import file are available in AWS Application Discovery Service. </p>"""
    group_id: NotRequired["aws_sdk_migrationhubstrategy.types.group_ids.GroupIds"]
    """<p>Groups the resources in the import file together with a unique name. This ID can be as filter in <code>ListApplicationComponents</code> and <code>ListServers</code>. </p>"""
    s3bucket_for_report_data: NotRequired[
        "aws_sdk_migrationhubstrategy.types.string.String"
    ]
    """<p> The S3 bucket where Strategy Recommendations uploads import results. The bucket name is required to begin with migrationhub-strategy-. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportFileTaskRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["S3Bucket"] = value["s3_bucket"]
    out["s3key"] = value["s3key"]
    if "data_source_type" in value:
        out["dataSourceType"] = value["data_source_type"]
    if "group_id" in value:
        import aws_sdk_migrationhubstrategy.types.group_ids

        out["groupId"] = aws_sdk_migrationhubstrategy.types.group_ids.serialize_json(
            value["group_id"]
        )
    if "s3bucket_for_report_data" in value:
        out["s3bucketForReportData"] = value["s3bucket_for_report_data"]
    return out


def deserialize_json(data: dict) -> StartImportFileTaskRequest:
    out: StartImportFileTaskRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StartImportFileTaskRequest.name required")
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        raise DeserializationError("StartImportFileTaskRequest.s3_bucket required")
    if "s3key" in data:
        out["s3key"] = data["s3key"]
    else:
        raise DeserializationError("StartImportFileTaskRequest.s3key required")
    if "dataSourceType" in data:
        out["data_source_type"] = data["dataSourceType"]
    if "groupId" in data:
        import aws_sdk_migrationhubstrategy.types.group_ids

        out["group_id"] = aws_sdk_migrationhubstrategy.types.group_ids.deserialize_json(
            data["groupId"]
        )
    if "s3bucketForReportData" in data:
        out["s3bucket_for_report_data"] = data["s3bucketForReportData"]
    return out
