"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#CreateBatchLoadTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.client_request_token
    import aws_sdk_timestream_write.types.data_model_configuration
    import aws_sdk_timestream_write.types.data_source_configuration
    import aws_sdk_timestream_write.types.record_version
    import aws_sdk_timestream_write.types.report_configuration
    import aws_sdk_timestream_write.types.resource_create_api_name


class CreateBatchLoadTaskRequest(TypedDict):
    client_token: NotRequired[
        "aws_sdk_timestream_write.types.client_request_token.ClientRequestToken"
    ]
    """<p></p>"""
    data_model_configuration: NotRequired[
        "aws_sdk_timestream_write.types.data_model_configuration.DataModelConfiguration"
    ]
    data_source_configuration: "aws_sdk_timestream_write.types.data_source_configuration.DataSourceConfiguration"
    """<p>Defines configuration details about the data source for a batch load task.</p>"""
    report_configuration: (
        "aws_sdk_timestream_write.types.report_configuration.ReportConfiguration"
    )
    target_database_name: (
        "aws_sdk_timestream_write.types.resource_create_api_name.ResourceCreateAPIName"
    )
    """<p>Target Timestream database for a batch load task.</p>"""
    target_table_name: (
        "aws_sdk_timestream_write.types.resource_create_api_name.ResourceCreateAPIName"
    )
    """<p>Target Timestream table for a batch load task.</p>"""
    record_version: NotRequired[
        "aws_sdk_timestream_write.types.record_version.RecordVersion"
    ]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBatchLoadTaskRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "data_model_configuration" in value:
        import aws_sdk_timestream_write.types.data_model_configuration

        out["DataModelConfiguration"] = (
            aws_sdk_timestream_write.types.data_model_configuration.serialize_aws_json_1_0(
                value["data_model_configuration"]
            )
        )
    import aws_sdk_timestream_write.types.data_source_configuration

    out["DataSourceConfiguration"] = (
        aws_sdk_timestream_write.types.data_source_configuration.serialize_aws_json_1_0(
            value["data_source_configuration"]
        )
    )
    import aws_sdk_timestream_write.types.report_configuration

    out["ReportConfiguration"] = (
        aws_sdk_timestream_write.types.report_configuration.serialize_aws_json_1_0(
            value["report_configuration"]
        )
    )
    out["TargetDatabaseName"] = value["target_database_name"]
    out["TargetTableName"] = value["target_table_name"]
    if "record_version" in value:
        out["RecordVersion"] = value["record_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateBatchLoadTaskRequest:
    out: CreateBatchLoadTaskRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "DataModelConfiguration" in data:
        import aws_sdk_timestream_write.types.data_model_configuration

        out["data_model_configuration"] = (
            aws_sdk_timestream_write.types.data_model_configuration.deserialize_aws_json_1_0(
                data["DataModelConfiguration"]
            )
        )
    if "DataSourceConfiguration" in data:
        import aws_sdk_timestream_write.types.data_source_configuration

        out["data_source_configuration"] = (
            aws_sdk_timestream_write.types.data_source_configuration.deserialize_aws_json_1_0(
                data["DataSourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBatchLoadTaskRequest.data_source_configuration required"
        )
    if "ReportConfiguration" in data:
        import aws_sdk_timestream_write.types.report_configuration

        out["report_configuration"] = (
            aws_sdk_timestream_write.types.report_configuration.deserialize_aws_json_1_0(
                data["ReportConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBatchLoadTaskRequest.report_configuration required"
        )
    if "TargetDatabaseName" in data:
        out["target_database_name"] = data["TargetDatabaseName"]
    else:
        raise DeserializationError(
            "CreateBatchLoadTaskRequest.target_database_name required"
        )
    if "TargetTableName" in data:
        out["target_table_name"] = data["TargetTableName"]
    else:
        raise DeserializationError(
            "CreateBatchLoadTaskRequest.target_table_name required"
        )
    if "RecordVersion" in data:
        out["record_version"] = data["RecordVersion"]
    return out
