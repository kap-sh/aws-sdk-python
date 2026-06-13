"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunSummary``."""

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
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.run_statistics_for_assets


class DataSourceRunSummary(TypedDict):
    id: "aws_sdk_datazone.types.data_source_run_id.DataSourceRunId"
    """<p>The identifier of the data source run.</p>"""
    data_source_id: "aws_sdk_datazone.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source of the data source run.</p>"""
    type: "aws_sdk_datazone.types.data_source_run_type.DataSourceRunType"
    """<p>The type of the data source run.</p>"""
    status: "aws_sdk_datazone.types.data_source_run_status.DataSourceRunStatus"
    """<p>The status of the data source run.</p>"""
    project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The project ID of the data source run.</p>"""
    run_statistics_for_assets: NotRequired[
        "aws_sdk_datazone.types.run_statistics_for_assets.RunStatisticsForAssets"
    ]
    error_message: NotRequired[
        "aws_sdk_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    created_at: "aws_sdk_datazone.types.date_time.DateTime"
    """<p>The timestamp of when a data source run was created.</p>"""
    updated_at: "aws_sdk_datazone.types.date_time.DateTime"
    """<p>The timestamp of when a data source run was updated.</p>"""
    started_at: NotRequired["aws_sdk_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when a data source run was started.</p>"""
    stopped_at: NotRequired["aws_sdk_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when a data source run was stopped.</p>"""
    lineage_summary: NotRequired[
        "aws_sdk_datazone.types.data_source_run_lineage_summary.DataSourceRunLineageSummary"
    ]
    """<p>The run lineage summary of a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceRunSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["dataSourceId"] = value["data_source_id"]
    import aws_sdk_datazone.types.data_source_run_type

    out["type"] = aws_sdk_datazone.types.data_source_run_type.serialize_json(
        value["type"]
    )
    import aws_sdk_datazone.types.data_source_run_status

    out["status"] = aws_sdk_datazone.types.data_source_run_status.serialize_json(
        value["status"]
    )
    out["projectId"] = value["project_id"]
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
    if "lineage_summary" in value:
        import aws_sdk_datazone.types.data_source_run_lineage_summary

        out["lineageSummary"] = (
            aws_sdk_datazone.types.data_source_run_lineage_summary.serialize_json(
                value["lineage_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceRunSummary:
    out: DataSourceRunSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DataSourceRunSummary.id required")
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    else:
        raise DeserializationError("DataSourceRunSummary.data_source_id required")
    if "type" in data:
        import aws_sdk_datazone.types.data_source_run_type

        out["type"] = aws_sdk_datazone.types.data_source_run_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("DataSourceRunSummary.type required")
    if "status" in data:
        import aws_sdk_datazone.types.data_source_run_status

        out["status"] = aws_sdk_datazone.types.data_source_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DataSourceRunSummary.status required")
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("DataSourceRunSummary.project_id required")
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
        raise DeserializationError("DataSourceRunSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_datazone.types.date_time

        out["updated_at"] = aws_sdk_datazone.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("DataSourceRunSummary.updated_at required")
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
    if "lineageSummary" in data:
        import aws_sdk_datazone.types.data_source_run_lineage_summary

        out["lineage_summary"] = (
            aws_sdk_datazone.types.data_source_run_lineage_summary.deserialize_json(
                data["lineageSummary"]
            )
        )
    return out
