"""Generated from Smithy shape ``com.amazonaws.datazone#StartDataSourceRunOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_source_error_message
    import aws_sdk_datazone.types.data_source_id
    import aws_sdk_datazone.types.data_source_run_id
    import aws_sdk_datazone.types.data_source_run_status
    import aws_sdk_datazone.types.data_source_run_type
    import aws_sdk_datazone.types.date_time
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.run_statistics_for_assets


class StartDataSourceRunOutput(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which to start a data source run.</p>"""
    data_source_id: "aws_sdk_datazone.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source.</p>"""
    id: "aws_sdk_datazone.types.data_source_run_id.DataSourceRunId"
    """<p>The identifier of the data source run.</p>"""
    project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project.</p>"""
    status: "aws_sdk_datazone.types.data_source_run_status.DataSourceRunStatus"
    """<p>The status of the data source run.</p>"""
    type: "aws_sdk_datazone.types.data_source_run_type.DataSourceRunType"
    """<p>The type of the data source run.</p>"""
    data_source_configuration_snapshot: NotRequired["str"]
    """<p>The configuration snapshot of the data source that is being run.</p>"""
    run_statistics_for_assets: NotRequired[
        "aws_sdk_datazone.types.run_statistics_for_assets.RunStatisticsForAssets"
    ]
    """<p>Specifies run statistics for assets.</p>"""
    error_message: NotRequired[
        "aws_sdk_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    created_at: "aws_sdk_datazone.types.date_time.DateTime"
    """<p>The timestamp of when data source run was created.</p>"""
    updated_at: "aws_sdk_datazone.types.date_time.DateTime"
    """<p>The timestamp of when the data source run was updated.</p>"""
    started_at: NotRequired["aws_sdk_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when the data source run was started.</p>"""
    stopped_at: NotRequired["aws_sdk_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when the data source run was stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDataSourceRunOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["dataSourceId"] = value["data_source_id"]
    out["id"] = value["id"]
    out["projectId"] = value["project_id"]
    import aws_sdk_datazone.types.data_source_run_status

    out["status"] = aws_sdk_datazone.types.data_source_run_status.serialize_json(
        value["status"]
    )
    import aws_sdk_datazone.types.data_source_run_type

    out["type"] = aws_sdk_datazone.types.data_source_run_type.serialize_json(
        value["type"]
    )
    if "data_source_configuration_snapshot" in value:
        out["dataSourceConfigurationSnapshot"] = value[
            "data_source_configuration_snapshot"
        ]
    if "run_statistics_for_assets" in value:
        import aws_sdk_datazone.types.run_statistics_for_assets

        out["runStatisticsForAssets"] = (
            aws_sdk_datazone.types.run_statistics_for_assets.serialize_json(
                value["run_statistics_for_assets"]
            )
        )
    if "error_message" in value:
        import aws_sdk_datazone.types.data_source_error_message

        out["errorMessage"] = (
            aws_sdk_datazone.types.data_source_error_message.serialize_json(
                value["error_message"]
            )
        )
    import aws_sdk_datazone.types.date_time

    out["createdAt"] = aws_sdk_datazone.types.date_time.serialize_json(
        value["created_at"]
    )
    import aws_sdk_datazone.types.date_time

    out["updatedAt"] = aws_sdk_datazone.types.date_time.serialize_json(
        value["updated_at"]
    )
    if "started_at" in value:
        import aws_sdk_datazone.types.date_time

        out["startedAt"] = aws_sdk_datazone.types.date_time.serialize_json(
            value["started_at"]
        )
    if "stopped_at" in value:
        import aws_sdk_datazone.types.date_time

        out["stoppedAt"] = aws_sdk_datazone.types.date_time.serialize_json(
            value["stopped_at"]
        )
    return out


def deserialize_json(data: dict) -> StartDataSourceRunOutput:
    out: StartDataSourceRunOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("StartDataSourceRunOutput.domain_id required")
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    else:
        raise DeserializationError("StartDataSourceRunOutput.data_source_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StartDataSourceRunOutput.id required")
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("StartDataSourceRunOutput.project_id required")
    if "status" in data:
        import aws_sdk_datazone.types.data_source_run_status

        out["status"] = aws_sdk_datazone.types.data_source_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("StartDataSourceRunOutput.status required")
    if "type" in data:
        import aws_sdk_datazone.types.data_source_run_type

        out["type"] = aws_sdk_datazone.types.data_source_run_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("StartDataSourceRunOutput.type required")
    if "dataSourceConfigurationSnapshot" in data:
        out["data_source_configuration_snapshot"] = data[
            "dataSourceConfigurationSnapshot"
        ]
    if "runStatisticsForAssets" in data:
        import aws_sdk_datazone.types.run_statistics_for_assets

        out["run_statistics_for_assets"] = (
            aws_sdk_datazone.types.run_statistics_for_assets.deserialize_json(
                data["runStatisticsForAssets"]
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
    else:
        raise DeserializationError("StartDataSourceRunOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_datazone.types.date_time

        out["updated_at"] = aws_sdk_datazone.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("StartDataSourceRunOutput.updated_at required")
    if "startedAt" in data:
        import aws_sdk_datazone.types.date_time

        out["started_at"] = aws_sdk_datazone.types.date_time.deserialize_json(
            data["startedAt"]
        )
    if "stoppedAt" in data:
        import aws_sdk_datazone.types.date_time

        out["stopped_at"] = aws_sdk_datazone.types.date_time.deserialize_json(
            data["stoppedAt"]
        )
    return out
