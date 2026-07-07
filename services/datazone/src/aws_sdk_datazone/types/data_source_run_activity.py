"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunActivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_asset_activity_status
    import aws_sdk_datazone.types.data_source_error_message
    import aws_sdk_datazone.types.data_source_run_id
    import aws_sdk_datazone.types.date_time
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.lineage_info
    import aws_sdk_datazone.types.name
    import aws_sdk_datazone.types.project_id


class DataSourceRunActivity(TypedDict, closed=True):
    database: "aws_sdk_datazone.types.name.Name"
    """<p>The database included in the data source run activity.</p>"""
    data_source_run_id: "aws_sdk_datazone.types.data_source_run_id.DataSourceRunId"
    """<p>The identifier of the data source for the data source run activity.</p>"""
    technical_name: "aws_sdk_datazone.types.name.Name"
    """<p>The technical name included in the data source run activity.</p>"""
    data_asset_status: (
        "aws_sdk_datazone.types.data_asset_activity_status.DataAssetActivityStatus"
    )
    """<p>The status of the asset included in the data source run activity.</p>"""
    project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The project ID included in the data source run activity.</p>"""
    data_asset_id: NotRequired["str"]
    """<p>The identifier of the asset included in the data source run activity.</p>"""
    technical_description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The technical description included in the data source run activity.</p>"""
    error_message: NotRequired[
        "aws_sdk_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    lineage_summary: NotRequired["aws_sdk_datazone.types.lineage_info.LineageInfo"]
    """<p>The data lineage summary.</p>"""
    created_at: "aws_sdk_datazone.types.date_time.DateTime"
    """<p>The timestamp of when data source run activity was created.</p>"""
    updated_at: "aws_sdk_datazone.types.date_time.DateTime"
    """<p>The timestamp of when data source run activity was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceRunActivity) -> dict:
    out: dict = {}
    out["database"] = value["database"]
    out["dataSourceRunId"] = value["data_source_run_id"]
    out["technicalName"] = value["technical_name"]
    import aws_sdk_datazone.types.data_asset_activity_status

    out["dataAssetStatus"] = (
        aws_sdk_datazone.types.data_asset_activity_status.serialize_json(
            value["data_asset_status"]
        )
    )
    out["projectId"] = value["project_id"]
    if "data_asset_id" in value:
        out["dataAssetId"] = value["data_asset_id"]
    if "technical_description" in value:
        out["technicalDescription"] = value["technical_description"]
    if "error_message" in value:
        import aws_sdk_datazone.types.data_source_error_message

        out["errorMessage"] = (
            aws_sdk_datazone.types.data_source_error_message.serialize_json(
                value["error_message"]
            )
        )
    if "lineage_summary" in value:
        import aws_sdk_datazone.types.lineage_info

        out["lineageSummary"] = aws_sdk_datazone.types.lineage_info.serialize_json(
            value["lineage_summary"]
        )
    import aws_sdk_datazone.types.date_time

    out["createdAt"] = aws_sdk_datazone.types.date_time.serialize_json(
        value["created_at"]
    )
    import aws_sdk_datazone.types.date_time

    out["updatedAt"] = aws_sdk_datazone.types.date_time.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> DataSourceRunActivity:
    out: DataSourceRunActivity = {}  # type: ignore[typeddict-item]
    if "database" in data:
        out["database"] = data["database"]
    else:
        raise DeserializationError("DataSourceRunActivity.database required")
    if "dataSourceRunId" in data:
        out["data_source_run_id"] = data["dataSourceRunId"]
    else:
        raise DeserializationError("DataSourceRunActivity.data_source_run_id required")
    if "technicalName" in data:
        out["technical_name"] = data["technicalName"]
    else:
        raise DeserializationError("DataSourceRunActivity.technical_name required")
    if "dataAssetStatus" in data:
        import aws_sdk_datazone.types.data_asset_activity_status

        out["data_asset_status"] = (
            aws_sdk_datazone.types.data_asset_activity_status.deserialize_json(
                data["dataAssetStatus"]
            )
        )
    else:
        raise DeserializationError("DataSourceRunActivity.data_asset_status required")
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("DataSourceRunActivity.project_id required")
    if "dataAssetId" in data:
        out["data_asset_id"] = data["dataAssetId"]
    if "technicalDescription" in data:
        out["technical_description"] = data["technicalDescription"]
    if "errorMessage" in data:
        import aws_sdk_datazone.types.data_source_error_message

        out["error_message"] = (
            aws_sdk_datazone.types.data_source_error_message.deserialize_json(
                data["errorMessage"]
            )
        )
    if "lineageSummary" in data:
        import aws_sdk_datazone.types.lineage_info

        out["lineage_summary"] = aws_sdk_datazone.types.lineage_info.deserialize_json(
            data["lineageSummary"]
        )
    if "createdAt" in data:
        import aws_sdk_datazone.types.date_time

        out["created_at"] = aws_sdk_datazone.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("DataSourceRunActivity.created_at required")
    if "updatedAt" in data:
        import aws_sdk_datazone.types.date_time

        out["updated_at"] = aws_sdk_datazone.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("DataSourceRunActivity.updated_at required")
    return out
