"""Generated from Smithy shape ``com.amazonaws.datazone#GetDataSourceRunOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_source_error_message
    import aws_sdk_datazone.types.data_source_id
    import aws_sdk_datazone.types.data_source_run_id
    import aws_sdk_datazone.types.data_source_run_lineage_summary
    import aws_sdk_datazone.types.data_source_run_status
    import aws_sdk_datazone.types.data_source_run_type
    import aws_sdk_datazone.types.date_time
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.run_statistics_for_assets


class GetDataSourceRunOutput(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which this data source run was performed.</p>"""
    data_source_id: "aws_sdk_datazone.types.data_source_id.DataSourceId"
    """<p>The ID of the data source for this data source run.</p>"""
    id: "aws_sdk_datazone.types.data_source_run_id.DataSourceRunId"
    """<p>The ID of the data source run.</p>"""
    project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the project in which this data source run occured.</p>"""
    status: "aws_sdk_datazone.types.data_source_run_status.DataSourceRunStatus"
    """<p>The status of this data source run.</p>"""
    type: "aws_sdk_datazone.types.data_source_run_type.DataSourceRunType"
    """<p>The type of this data source run.</p>"""
    data_source_configuration_snapshot: NotRequired["str"]
    """<p>The configuration snapshot of the data source run.</p>"""
    run_statistics_for_assets: NotRequired[
        "aws_sdk_datazone.types.run_statistics_for_assets.RunStatisticsForAssets"
    ]
    """<p>The asset statistics from this data source run.</p>"""
    lineage_summary: NotRequired[
        "aws_sdk_datazone.types.data_source_run_lineage_summary.DataSourceRunLineageSummary"
    ]
    """<p>The summary of the data lineage.</p>"""
    error_message: NotRequired[
        "aws_sdk_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    created_at: "aws_sdk_datazone.types.date_time.DateTime"
    """<p>The timestamp of when the data source run was created.</p>"""
    updated_at: "aws_sdk_datazone.types.date_time.DateTime"
    """<p>The timestamp of when this data source run was updated.</p>"""
    started_at: NotRequired["aws_sdk_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when this data source run started.</p>"""
    stopped_at: NotRequired["aws_sdk_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when this data source run stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSourceRunOutput) -> dict:
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
    if "lineage_summary" in value:
        import aws_sdk_datazone.types.data_source_run_lineage_summary

        out["lineageSummary"] = (
            aws_sdk_datazone.types.data_source_run_lineage_summary.serialize_json(
                value["lineage_summary"]
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


def deserialize_json(data: dict) -> GetDataSourceRunOutput:
    out: GetDataSourceRunOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetDataSourceRunOutput.domain_id required")
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    else:
        raise DeserializationError("GetDataSourceRunOutput.data_source_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetDataSourceRunOutput.id required")
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("GetDataSourceRunOutput.project_id required")
    if "status" in data:
        import aws_sdk_datazone.types.data_source_run_status

        out["status"] = aws_sdk_datazone.types.data_source_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetDataSourceRunOutput.status required")
    if "type" in data:
        import aws_sdk_datazone.types.data_source_run_type

        out["type"] = aws_sdk_datazone.types.data_source_run_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("GetDataSourceRunOutput.type required")
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
    if "lineageSummary" in data:
        import aws_sdk_datazone.types.data_source_run_lineage_summary

        out["lineage_summary"] = (
            aws_sdk_datazone.types.data_source_run_lineage_summary.deserialize_json(
                data["lineageSummary"]
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
        raise DeserializationError("GetDataSourceRunOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_datazone.types.date_time

        out["updated_at"] = aws_sdk_datazone.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GetDataSourceRunOutput.updated_at required")
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
