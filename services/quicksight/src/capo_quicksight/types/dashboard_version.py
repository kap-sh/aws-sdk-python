"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.dashboard_error_list
    import capo_quicksight.types.data_set_arns_list
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.sheet_list
    import capo_quicksight.types.timestamp
    import capo_quicksight.types.version_description
    import capo_quicksight.types.version_number


class DashboardVersion(TypedDict, closed=True):
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that this dashboard version was created.</p>"""
    errors: NotRequired["capo_quicksight.types.dashboard_error_list.DashboardErrorList"]
    """<p>Errors associated with this dashboard version.</p>"""
    version_number: NotRequired["capo_quicksight.types.version_number.VersionNumber"]
    """<p>Version number for this version of the dashboard.</p>"""
    status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>The HTTP status of the request.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    source_entity_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>Source entity ARN.</p>"""
    data_set_arns: NotRequired[
        "capo_quicksight.types.data_set_arns_list.DataSetArnsList"
    ]
    """<p>The Amazon Resource Numbers (ARNs) for the datasets that are associated with this version of the dashboard.</p>"""
    description: NotRequired[
        "capo_quicksight.types.version_description.VersionDescription"
    ]
    """<p>Description.</p>"""
    theme_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN of the theme associated with a version of the dashboard.</p>"""
    sheets: NotRequired["capo_quicksight.types.sheet_list.SheetList"]
    """<p>A list of the associated sheets with the unique identifier and name of each sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardVersion) -> dict:
    out: dict = {}
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "errors" in value:
        import capo_quicksight.types.dashboard_error_list

        out["Errors"] = capo_quicksight.types.dashboard_error_list.serialize_json(
            value["errors"]
        )
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "status" in value:
        import capo_quicksight.types.resource_status

        out["Status"] = capo_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "source_entity_arn" in value:
        out["SourceEntityArn"] = value["source_entity_arn"]
    if "data_set_arns" in value:
        import capo_quicksight.types.data_set_arns_list

        out["DataSetArns"] = capo_quicksight.types.data_set_arns_list.serialize_json(
            value["data_set_arns"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "sheets" in value:
        import capo_quicksight.types.sheet_list

        out["Sheets"] = capo_quicksight.types.sheet_list.serialize_json(value["sheets"])
    return out


def deserialize_json(data: dict) -> DashboardVersion:
    out: DashboardVersion = {}  # type: ignore[typeddict-item]
    if "CreatedTime" in data:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "Errors" in data:
        import capo_quicksight.types.dashboard_error_list

        out["errors"] = capo_quicksight.types.dashboard_error_list.deserialize_json(
            data["Errors"]
        )
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    if "Status" in data:
        import capo_quicksight.types.resource_status

        out["status"] = capo_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "SourceEntityArn" in data:
        out["source_entity_arn"] = data["SourceEntityArn"]
    if "DataSetArns" in data:
        import capo_quicksight.types.data_set_arns_list

        out["data_set_arns"] = (
            capo_quicksight.types.data_set_arns_list.deserialize_json(
                data["DataSetArns"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ThemeArn" in data:
        out["theme_arn"] = data["ThemeArn"]
    if "Sheets" in data:
        import capo_quicksight.types.sheet_list

        out["sheets"] = capo_quicksight.types.sheet_list.deserialize_json(
            data["Sheets"]
        )
    return out
