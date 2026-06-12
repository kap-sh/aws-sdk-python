"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StartContinuousExportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.configurations_export_id
    import aws_sdk_application_discovery_service.types.data_source
    import aws_sdk_application_discovery_service.types.s3_bucket
    import aws_sdk_application_discovery_service.types.schema_storage_config
    import aws_sdk_application_discovery_service.types.time_stamp


class StartContinuousExportResponse(TypedDict):
    export_id: NotRequired[
        "aws_sdk_application_discovery_service.types.configurations_export_id.ConfigurationsExportId"
    ]
    """<p>The unique ID assigned to this export.</p>"""
    s3_bucket: NotRequired[
        "aws_sdk_application_discovery_service.types.s3_bucket.S3Bucket"
    ]
    """<p>The name of the s3 bucket where the export data parquet files are stored.</p>"""
    start_time: NotRequired[
        "aws_sdk_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>The timestamp representing when the continuous export was started.</p>"""
    data_source: NotRequired[
        "aws_sdk_application_discovery_service.types.data_source.DataSource"
    ]
    """<p>The type of data collector used to gather this data (currently only offered for AGENT).</p>"""
    schema_storage_config: NotRequired[
        "aws_sdk_application_discovery_service.types.schema_storage_config.SchemaStorageConfig"
    ]
    """<p>A dictionary which describes how the data is stored.</p> <ul> <li> <p> <code>databaseName</code> - the name of the Glue database used to store the schema.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartContinuousExportResponse) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["exportId"] = value["export_id"]
    if "s3_bucket" in value:
        out["s3Bucket"] = value["s3_bucket"]
    if "start_time" in value:
        import aws_sdk_application_discovery_service.types.time_stamp

        out["startTime"] = (
            aws_sdk_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "data_source" in value:
        import aws_sdk_application_discovery_service.types.data_source

        out["dataSource"] = (
            aws_sdk_application_discovery_service.types.data_source.serialize_aws_json_1_1(
                value["data_source"]
            )
        )
    if "schema_storage_config" in value:
        import aws_sdk_application_discovery_service.types.schema_storage_config

        out["schemaStorageConfig"] = (
            aws_sdk_application_discovery_service.types.schema_storage_config.serialize_aws_json_1_1(
                value["schema_storage_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartContinuousExportResponse:
    out: StartContinuousExportResponse = {}  # type: ignore[typeddict-item]
    if "exportId" in data:
        out["export_id"] = data["exportId"]
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    if "startTime" in data:
        import aws_sdk_application_discovery_service.types.time_stamp

        out["start_time"] = (
            aws_sdk_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if "dataSource" in data:
        import aws_sdk_application_discovery_service.types.data_source

        out["data_source"] = (
            aws_sdk_application_discovery_service.types.data_source.deserialize_aws_json_1_1(
                data["dataSource"]
            )
        )
    if "schemaStorageConfig" in data:
        import aws_sdk_application_discovery_service.types.schema_storage_config

        out["schema_storage_config"] = (
            aws_sdk_application_discovery_service.types.schema_storage_config.deserialize_aws_json_1_1(
                data["schemaStorageConfig"]
            )
        )
    return out
