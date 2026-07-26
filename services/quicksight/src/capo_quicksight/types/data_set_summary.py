"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.boolean
    import capo_quicksight.types.data_set_import_mode
    import capo_quicksight.types.data_set_use_as
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.row_level_permission_data_set
    import capo_quicksight.types.row_level_permission_data_set_map
    import capo_quicksight.types.timestamp


class DataSetSummary(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    data_set_id: NotRequired["capo_quicksight.types.resource_id.ResourceId"]
    """<p>The ID of the dataset.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>A display name for the dataset.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that this dataset was created.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The last time that this dataset was updated.</p>"""
    import_mode: NotRequired[
        "capo_quicksight.types.data_set_import_mode.DataSetImportMode"
    ]
    """<p>A value that indicates whether you want to import the data into SPICE.</p>"""
    row_level_permission_data_set: NotRequired[
        "capo_quicksight.types.row_level_permission_data_set.RowLevelPermissionDataSet"
    ]
    """<p>The row-level security configuration for the dataset in the legacy data preparation experience.</p>"""
    row_level_permission_data_set_map: NotRequired[
        "capo_quicksight.types.row_level_permission_data_set_map.RowLevelPermissionDataSetMap"
    ]
    """<p>The row-level security configuration for the dataset in the new data preparation experience.</p>"""
    row_level_permission_tag_configuration_applied: (
        "capo_quicksight.types.boolean.Boolean"
    )
    """<p>Whether or not the row level permission tags are applied.</p>"""
    column_level_permission_rules_applied: "capo_quicksight.types.boolean.Boolean"
    """<p>A value that indicates if the dataset has column level permission configured.</p>"""
    use_as: NotRequired["capo_quicksight.types.data_set_use_as.DataSetUseAs"]
    """<p>The usage of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "data_set_id" in value:
        out["DataSetId"] = value["data_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "import_mode" in value:
        import capo_quicksight.types.data_set_import_mode

        out["ImportMode"] = capo_quicksight.types.data_set_import_mode.serialize_json(
            value["import_mode"]
        )
    if "row_level_permission_data_set" in value:
        import capo_quicksight.types.row_level_permission_data_set

        out["RowLevelPermissionDataSet"] = (
            capo_quicksight.types.row_level_permission_data_set.serialize_json(
                value["row_level_permission_data_set"]
            )
        )
    if "row_level_permission_data_set_map" in value:
        import capo_quicksight.types.row_level_permission_data_set_map

        out["RowLevelPermissionDataSetMap"] = (
            capo_quicksight.types.row_level_permission_data_set_map.serialize_json(
                value["row_level_permission_data_set_map"]
            )
        )
    out["RowLevelPermissionTagConfigurationApplied"] = value.get(
        "row_level_permission_tag_configuration_applied", False
    )
    out["ColumnLevelPermissionRulesApplied"] = value.get(
        "column_level_permission_rules_applied", False
    )
    if "use_as" in value:
        import capo_quicksight.types.data_set_use_as

        out["UseAs"] = capo_quicksight.types.data_set_use_as.serialize_json(
            value["use_as"]
        )
    return out


def deserialize_json(data: dict) -> DataSetSummary:
    out: DataSetSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatedTime" in data:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "ImportMode" in data:
        import capo_quicksight.types.data_set_import_mode

        out["import_mode"] = (
            capo_quicksight.types.data_set_import_mode.deserialize_json(
                data["ImportMode"]
            )
        )
    if "RowLevelPermissionDataSet" in data:
        import capo_quicksight.types.row_level_permission_data_set

        out["row_level_permission_data_set"] = (
            capo_quicksight.types.row_level_permission_data_set.deserialize_json(
                data["RowLevelPermissionDataSet"]
            )
        )
    if "RowLevelPermissionDataSetMap" in data:
        import capo_quicksight.types.row_level_permission_data_set_map

        out["row_level_permission_data_set_map"] = (
            capo_quicksight.types.row_level_permission_data_set_map.deserialize_json(
                data["RowLevelPermissionDataSetMap"]
            )
        )
    if "RowLevelPermissionTagConfigurationApplied" in data:
        out["row_level_permission_tag_configuration_applied"] = data[
            "RowLevelPermissionTagConfigurationApplied"
        ]
    else:
        out["row_level_permission_tag_configuration_applied"] = False
    if "ColumnLevelPermissionRulesApplied" in data:
        out["column_level_permission_rules_applied"] = data[
            "ColumnLevelPermissionRulesApplied"
        ]
    else:
        out["column_level_permission_rules_applied"] = False
    if "UseAs" in data:
        import capo_quicksight.types.data_set_use_as

        out["use_as"] = capo_quicksight.types.data_set_use_as.deserialize_json(
            data["UseAs"]
        )
    return out
