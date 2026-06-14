"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_source_error_message
    import aws_sdk_datazone.types.data_source_id
    import aws_sdk_datazone.types.data_source_run_status
    import aws_sdk_datazone.types.data_source_status
    import aws_sdk_datazone.types.date_time
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.enable_setting
    import aws_sdk_datazone.types.name
    import aws_sdk_datazone.types.schedule_configuration


class DataSourceSummary(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the data source exists.</p>"""
    environment_id: NotRequired["str"]
    """<p>The ID of the environment in which the data source exists.</p>"""
    connection_id: NotRequired["str"]
    """<p>The connection ID that's part of the data source summary.</p>"""
    data_source_id: "aws_sdk_datazone.types.data_source_id.DataSourceId"
    """<p>The ID of the data source.</p>"""
    name: "aws_sdk_datazone.types.name.Name"
    """<p>The name of the data source.</p>"""
    type: "str"
    """<p>The type of the data source.</p>"""
    status: "aws_sdk_datazone.types.data_source_status.DataSourceStatus"
    """<p>The status of the data source.</p>"""
    enable_setting: NotRequired["aws_sdk_datazone.types.enable_setting.EnableSetting"]
    """<p>Specifies whether the data source is enabled.</p>"""
    schedule: NotRequired[
        "aws_sdk_datazone.types.schedule_configuration.ScheduleConfiguration"
    ]
    last_run_status: NotRequired[
        "aws_sdk_datazone.types.data_source_run_status.DataSourceRunStatus"
    ]
    """<p>The status of the last data source run.</p>"""
    last_run_at: NotRequired["aws_sdk_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when the data source run was last performed.</p>"""
    last_run_error_message: NotRequired[
        "aws_sdk_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    last_run_asset_count: NotRequired["int"]
    """<p>The count of the assets created during the last data source run.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when the data source was created.</p>"""
    updated_at: NotRequired["aws_sdk_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when the data source was updated.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The data source description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSummary) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    out["dataSourceId"] = value["data_source_id"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    import aws_sdk_datazone.types.data_source_status

    out["status"] = aws_sdk_datazone.types.data_source_status.serialize_json(
        value["status"]
    )
    if "enable_setting" in value:
        import aws_sdk_datazone.types.enable_setting

        out["enableSetting"] = aws_sdk_datazone.types.enable_setting.serialize_json(
            value["enable_setting"]
        )
    if "schedule" in value:
        import aws_sdk_datazone.types.schedule_configuration

        out["schedule"] = aws_sdk_datazone.types.schedule_configuration.serialize_json(
            value["schedule"]
        )
    if "last_run_status" in value:
        import aws_sdk_datazone.types.data_source_run_status

        out["lastRunStatus"] = (
            aws_sdk_datazone.types.data_source_run_status.serialize_json(
                value["last_run_status"]
            )
        )
    if "last_run_at" in value:
        import aws_sdk_datazone.types.date_time

        out["lastRunAt"] = aws_sdk_datazone.types.date_time.serialize_json(
            value["last_run_at"]
        )
    if "last_run_error_message" in value:
        import aws_sdk_datazone.types.data_source_error_message

        out["lastRunErrorMessage"] = (
            aws_sdk_datazone.types.data_source_error_message.serialize_json(
                value["last_run_error_message"]
            )
        )
    if "last_run_asset_count" in value:
        out["lastRunAssetCount"] = value["last_run_asset_count"]
    if "created_at" in value:
        import aws_sdk_datazone.types.date_time

        out["createdAt"] = aws_sdk_datazone.types.date_time.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_datazone.types.date_time

        out["updatedAt"] = aws_sdk_datazone.types.date_time.serialize_json(
            value["updated_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> DataSourceSummary:
    out: DataSourceSummary = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("DataSourceSummary.domain_id required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    else:
        raise DeserializationError("DataSourceSummary.data_source_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DataSourceSummary.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("DataSourceSummary.type required")
    if "status" in data:
        import aws_sdk_datazone.types.data_source_status

        out["status"] = aws_sdk_datazone.types.data_source_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DataSourceSummary.status required")
    if "enableSetting" in data:
        import aws_sdk_datazone.types.enable_setting

        out["enable_setting"] = aws_sdk_datazone.types.enable_setting.deserialize_json(
            data["enableSetting"]
        )
    if "schedule" in data:
        import aws_sdk_datazone.types.schedule_configuration

        out["schedule"] = (
            aws_sdk_datazone.types.schedule_configuration.deserialize_json(
                data["schedule"]
            )
        )
    if "lastRunStatus" in data:
        import aws_sdk_datazone.types.data_source_run_status

        out["last_run_status"] = (
            aws_sdk_datazone.types.data_source_run_status.deserialize_json(
                data["lastRunStatus"]
            )
        )
    if "lastRunAt" in data:
        import aws_sdk_datazone.types.date_time

        out["last_run_at"] = aws_sdk_datazone.types.date_time.deserialize_json(
            data["lastRunAt"]
        )
    if "lastRunErrorMessage" in data:
        import aws_sdk_datazone.types.data_source_error_message

        out["last_run_error_message"] = (
            aws_sdk_datazone.types.data_source_error_message.deserialize_json(
                data["lastRunErrorMessage"]
            )
        )
    if "lastRunAssetCount" in data:
        out["last_run_asset_count"] = data["lastRunAssetCount"]
    if "createdAt" in data:
        import aws_sdk_datazone.types.date_time

        out["created_at"] = aws_sdk_datazone.types.date_time.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_datazone.types.date_time

        out["updated_at"] = aws_sdk_datazone.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
