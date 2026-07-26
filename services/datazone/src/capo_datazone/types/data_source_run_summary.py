"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.data_source_error_message
    import capo_datazone.types.data_source_id
    import capo_datazone.types.data_source_run_id
    import capo_datazone.types.data_source_run_lineage_summary
    import capo_datazone.types.data_source_run_status
    import capo_datazone.types.data_source_run_type
    import capo_datazone.types.date_time
    import capo_datazone.types.project_id
    import capo_datazone.types.run_statistics_for_assets


class DataSourceRunSummary(TypedDict, closed=True):
    id: "capo_datazone.types.data_source_run_id.DataSourceRunId"
    """<p>The identifier of the data source run.</p>"""
    data_source_id: "capo_datazone.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source of the data source run.</p>"""
    type: "capo_datazone.types.data_source_run_type.DataSourceRunType"
    """<p>The type of the data source run.</p>"""
    status: "capo_datazone.types.data_source_run_status.DataSourceRunStatus"
    """<p>The status of the data source run.</p>"""
    project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The project ID of the data source run.</p>"""
    run_statistics_for_assets: NotRequired[
        "capo_datazone.types.run_statistics_for_assets.RunStatisticsForAssets"
    ]
    error_message: NotRequired[
        "capo_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    created_at: "capo_datazone.types.date_time.DateTime"
    """<p>The timestamp of when a data source run was created.</p>"""
    updated_at: "capo_datazone.types.date_time.DateTime"
    """<p>The timestamp of when a data source run was updated.</p>"""
    started_at: NotRequired["capo_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when a data source run was started.</p>"""
    stopped_at: NotRequired["capo_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when a data source run was stopped.</p>"""
    lineage_summary: NotRequired[
        "capo_datazone.types.data_source_run_lineage_summary.DataSourceRunLineageSummary"
    ]
    """<p>The run lineage summary of a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceRunSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["dataSourceId"] = value["data_source_id"]
    import capo_datazone.types.data_source_run_type

    out["type"] = capo_datazone.types.data_source_run_type.serialize_json(value["type"])
    import capo_datazone.types.data_source_run_status

    out["status"] = capo_datazone.types.data_source_run_status.serialize_json(
        value["status"]
    )
    out["projectId"] = value["project_id"]
    if "run_statistics_for_assets" in value:
        import capo_datazone.types.run_statistics_for_assets

        out["runStatisticsForAssets"] = (
            capo_datazone.types.run_statistics_for_assets.serialize_json(
                value["run_statistics_for_assets"]
            )
        )
    if "error_message" in value:
        import capo_datazone.types.data_source_error_message

        out["errorMessage"] = (
            capo_datazone.types.data_source_error_message.serialize_json(
                value["error_message"]
            )
        )
    import capo_datazone.types.date_time

    out["createdAt"] = capo_datazone.types.date_time.serialize_json(value["created_at"])
    import capo_datazone.types.date_time

    out["updatedAt"] = capo_datazone.types.date_time.serialize_json(value["updated_at"])
    if "started_at" in value:
        import capo_datazone.types.date_time

        out["startedAt"] = capo_datazone.types.date_time.serialize_json(
            value["started_at"]
        )
    if "stopped_at" in value:
        import capo_datazone.types.date_time

        out["stoppedAt"] = capo_datazone.types.date_time.serialize_json(
            value["stopped_at"]
        )
    if "lineage_summary" in value:
        import capo_datazone.types.data_source_run_lineage_summary

        out["lineageSummary"] = (
            capo_datazone.types.data_source_run_lineage_summary.serialize_json(
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
        import capo_datazone.types.data_source_run_type

        out["type"] = capo_datazone.types.data_source_run_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("DataSourceRunSummary.type required")
    if "status" in data:
        import capo_datazone.types.data_source_run_status

        out["status"] = capo_datazone.types.data_source_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DataSourceRunSummary.status required")
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("DataSourceRunSummary.project_id required")
    if "runStatisticsForAssets" in data:
        import capo_datazone.types.run_statistics_for_assets

        out["run_statistics_for_assets"] = (
            capo_datazone.types.run_statistics_for_assets.deserialize_json(
                data["runStatisticsForAssets"]
            )
        )
    if "errorMessage" in data:
        import capo_datazone.types.data_source_error_message

        out["error_message"] = (
            capo_datazone.types.data_source_error_message.deserialize_json(
                data["errorMessage"]
            )
        )
    if "createdAt" in data:
        import capo_datazone.types.date_time

        out["created_at"] = capo_datazone.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("DataSourceRunSummary.created_at required")
    if "updatedAt" in data:
        import capo_datazone.types.date_time

        out["updated_at"] = capo_datazone.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("DataSourceRunSummary.updated_at required")
    if "startedAt" in data:
        import capo_datazone.types.date_time

        out["started_at"] = capo_datazone.types.date_time.deserialize_json(
            data["startedAt"]
        )
    if "stoppedAt" in data:
        import capo_datazone.types.date_time

        out["stopped_at"] = capo_datazone.types.date_time.deserialize_json(
            data["stoppedAt"]
        )
    if "lineageSummary" in data:
        import capo_datazone.types.data_source_run_lineage_summary

        out["lineage_summary"] = (
            capo_datazone.types.data_source_run_lineage_summary.deserialize_json(
                data["lineageSummary"]
            )
        )
    return out
