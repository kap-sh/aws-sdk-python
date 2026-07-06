"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDataSourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_source_configuration_output
    import aws_sdk_datazone.types.data_source_error_message
    import aws_sdk_datazone.types.data_source_id
    import aws_sdk_datazone.types.data_source_run_status
    import aws_sdk_datazone.types.data_source_status
    import aws_sdk_datazone.types.data_source_type
    import aws_sdk_datazone.types.date_time
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.enable_setting
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.form_output_list
    import aws_sdk_datazone.types.name
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.recommendation_configuration
    import aws_sdk_datazone.types.schedule_configuration


class CreateDataSourceOutput(TypedDict, closed=True):
    id: "aws_sdk_datazone.types.data_source_id.DataSourceId"
    """<p>The unique identifier of the data source.</p>"""
    status: NotRequired["aws_sdk_datazone.types.data_source_status.DataSourceStatus"]
    """<p>The status of the data source.</p>"""
    type: NotRequired["aws_sdk_datazone.types.data_source_type.DataSourceType"]
    """<p>The type of the data source.</p>"""
    name: "aws_sdk_datazone.types.name.Name"
    """<p>The name of the data source.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the data source.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the data source is created.</p>"""
    project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the Amazon DataZone project to which the data source is added.</p>"""
    environment_id: NotRequired["aws_sdk_datazone.types.environment_id.EnvironmentId"]
    """<p>The unique identifier of the Amazon DataZone environment to which the data source publishes assets. </p>"""
    connection_id: NotRequired["str"]
    """<p>The ID of the connection.</p>"""
    configuration: NotRequired[
        "aws_sdk_datazone.types.data_source_configuration_output.DataSourceConfigurationOutput"
    ]
    """<p>Specifies the configuration of the data source. It can be set to either <code>glueRunConfiguration</code> or <code>redshiftRunConfiguration</code>.</p>"""
    recommendation: NotRequired[
        "aws_sdk_datazone.types.recommendation_configuration.RecommendationConfiguration"
    ]
    """<p>Specifies whether the business name generation is to be enabled for this data source.</p>"""
    enable_setting: NotRequired["aws_sdk_datazone.types.enable_setting.EnableSetting"]
    """<p>Specifies whether the data source is enabled.</p>"""
    publish_on_import: NotRequired["bool"]
    """<p>Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.</p>"""
    asset_forms_output: NotRequired[
        "aws_sdk_datazone.types.form_output_list.FormOutputList"
    ]
    """<p>The metadata forms attached to the assets that this data source creates.</p>"""
    schedule: NotRequired[
        "aws_sdk_datazone.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The schedule of the data source runs.</p>"""
    last_run_status: NotRequired[
        "aws_sdk_datazone.types.data_source_run_status.DataSourceRunStatus"
    ]
    """<p>The status of the last run of this data source.</p>"""
    last_run_at: NotRequired["aws_sdk_datazone.types.date_time.DateTime"]
    """<p>The timestamp that specifies when the data source was last run.</p>"""
    last_run_error_message: NotRequired[
        "aws_sdk_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    error_message: NotRequired[
        "aws_sdk_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when the data source was created.</p>"""
    updated_at: NotRequired["aws_sdk_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when the data source was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSourceOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "status" in value:
        import aws_sdk_datazone.types.data_source_status

        out["status"] = aws_sdk_datazone.types.data_source_status.serialize_json(
            value["status"]
        )
    if "type" in value:
        out["type"] = value["type"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["domainId"] = value["domain_id"]
    out["projectId"] = value["project_id"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "configuration" in value:
        import aws_sdk_datazone.types.data_source_configuration_output

        out["configuration"] = (
            aws_sdk_datazone.types.data_source_configuration_output.serialize_json(
                value["configuration"]
            )
        )
    if "recommendation" in value:
        import aws_sdk_datazone.types.recommendation_configuration

        out["recommendation"] = (
            aws_sdk_datazone.types.recommendation_configuration.serialize_json(
                value["recommendation"]
            )
        )
    if "enable_setting" in value:
        import aws_sdk_datazone.types.enable_setting

        out["enableSetting"] = aws_sdk_datazone.types.enable_setting.serialize_json(
            value["enable_setting"]
        )
    if "publish_on_import" in value:
        out["publishOnImport"] = value["publish_on_import"]
    if "asset_forms_output" in value:
        import aws_sdk_datazone.types.form_output_list

        out["assetFormsOutput"] = (
            aws_sdk_datazone.types.form_output_list.serialize_json(
                value["asset_forms_output"]
            )
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
    if "error_message" in value:
        import aws_sdk_datazone.types.data_source_error_message

        out["errorMessage"] = (
            aws_sdk_datazone.types.data_source_error_message.serialize_json(
                value["error_message"]
            )
        )
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
    return out


def deserialize_json(data: dict) -> CreateDataSourceOutput:
    out: CreateDataSourceOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateDataSourceOutput.id required")
    if "status" in data:
        import aws_sdk_datazone.types.data_source_status

        out["status"] = aws_sdk_datazone.types.data_source_status.deserialize_json(
            data["status"]
        )
    if "type" in data:
        out["type"] = data["type"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDataSourceOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateDataSourceOutput.domain_id required")
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("CreateDataSourceOutput.project_id required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    if "configuration" in data:
        import aws_sdk_datazone.types.data_source_configuration_output

        out["configuration"] = (
            aws_sdk_datazone.types.data_source_configuration_output.deserialize_json(
                data["configuration"]
            )
        )
    if "recommendation" in data:
        import aws_sdk_datazone.types.recommendation_configuration

        out["recommendation"] = (
            aws_sdk_datazone.types.recommendation_configuration.deserialize_json(
                data["recommendation"]
            )
        )
    if "enableSetting" in data:
        import aws_sdk_datazone.types.enable_setting

        out["enable_setting"] = aws_sdk_datazone.types.enable_setting.deserialize_json(
            data["enableSetting"]
        )
    if "publishOnImport" in data:
        out["publish_on_import"] = data["publishOnImport"]
    if "assetFormsOutput" in data:
        import aws_sdk_datazone.types.form_output_list

        out["asset_forms_output"] = (
            aws_sdk_datazone.types.form_output_list.deserialize_json(
                data["assetFormsOutput"]
            )
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
    if "errorMessage" in data:
        import aws_sdk_datazone.types.data_source_error_message

        out["error_message"] = (
            aws_sdk_datazone.types.data_source_error_message.deserialize_json(
                data["errorMessage"]
            )
        )
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
    return out
