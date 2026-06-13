"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDataSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.column_group_list
    import aws_sdk_quicksight.types.column_level_permission_rule_list
    import aws_sdk_quicksight.types.data_prep_configuration
    import aws_sdk_quicksight.types.data_set_import_mode
    import aws_sdk_quicksight.types.data_set_usage_configuration
    import aws_sdk_quicksight.types.dataset_parameter_list
    import aws_sdk_quicksight.types.field_folder_map
    import aws_sdk_quicksight.types.logical_table_map
    import aws_sdk_quicksight.types.performance_configuration
    import aws_sdk_quicksight.types.physical_table_map
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.resource_name
    import aws_sdk_quicksight.types.row_level_permission_data_set
    import aws_sdk_quicksight.types.row_level_permission_tag_configuration
    import aws_sdk_quicksight.types.semantic_model_configuration


class UpdateDataSetRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    data_set_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID for the dataset that you want to update. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    name: "aws_sdk_quicksight.types.resource_name.ResourceName"
    """<p>The display name for the dataset.</p>"""
    physical_table_map: "aws_sdk_quicksight.types.physical_table_map.PhysicalTableMap"
    """<p>Declares the physical tables that are available in the underlying data sources.</p>"""
    logical_table_map: NotRequired[
        "aws_sdk_quicksight.types.logical_table_map.LogicalTableMap"
    ]
    """<p>Configures the combination and transformation of the data from the physical tables. This parameter is used with the legacy data preparation experience.</p>"""
    import_mode: "aws_sdk_quicksight.types.data_set_import_mode.DataSetImportMode"
    """<p>Indicates whether you want to import the data into SPICE.</p>"""
    column_groups: NotRequired[
        "aws_sdk_quicksight.types.column_group_list.ColumnGroupList"
    ]
    """<p>Groupings of columns that work together in certain Amazon Quick Sight features. Currently, only geospatial hierarchy is supported.</p>"""
    field_folders: NotRequired[
        "aws_sdk_quicksight.types.field_folder_map.FieldFolderMap"
    ]
    """<p>The folder that contains fields and nested subfolders for your dataset.</p>"""
    row_level_permission_data_set: NotRequired[
        "aws_sdk_quicksight.types.row_level_permission_data_set.RowLevelPermissionDataSet"
    ]
    """<p>The row-level security configuration for the data you want to create. This parameter is used with the legacy data preparation experience.</p>"""
    row_level_permission_tag_configuration: NotRequired[
        "aws_sdk_quicksight.types.row_level_permission_tag_configuration.RowLevelPermissionTagConfiguration"
    ]
    """<p>The configuration of tags on a dataset to set row-level security. Row-level security tags are currently supported for anonymous embedding only. This parameter is used with the legacy data preparation experience.</p>"""
    column_level_permission_rules: NotRequired[
        "aws_sdk_quicksight.types.column_level_permission_rule_list.ColumnLevelPermissionRuleList"
    ]
    """<p>A set of one or more definitions of a <code> <a href=\"https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnLevelPermissionRule.html\">ColumnLevelPermissionRule</a> </code>.</p>"""
    data_set_usage_configuration: NotRequired[
        "aws_sdk_quicksight.types.data_set_usage_configuration.DataSetUsageConfiguration"
    ]
    dataset_parameters: NotRequired[
        "aws_sdk_quicksight.types.dataset_parameter_list.DatasetParameterList"
    ]
    """<p>The parameter declarations of the dataset.</p>"""
    performance_configuration: NotRequired[
        "aws_sdk_quicksight.types.performance_configuration.PerformanceConfiguration"
    ]
    """<p>The configuration for the performance optimization of the dataset that contains a <code>UniqueKey</code> configuration.</p>"""
    data_prep_configuration: NotRequired[
        "aws_sdk_quicksight.types.data_prep_configuration.DataPrepConfiguration"
    ]
    """<p>The data preparation configuration for the dataset. This configuration defines the source tables, transformation steps, and destination tables used to prepare the data. Required when using the new data preparation experience.</p>"""
    semantic_model_configuration: NotRequired[
        "aws_sdk_quicksight.types.semantic_model_configuration.SemanticModelConfiguration"
    ]
    """<p>The semantic model configuration for the dataset. This configuration defines how the prepared data is structured for an analysis, including table mappings and row-level security configurations. Required when using the new data preparation experience.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_quicksight.types.physical_table_map

    out["PhysicalTableMap"] = (
        aws_sdk_quicksight.types.physical_table_map.serialize_json(
            value["physical_table_map"]
        )
    )
    if "logical_table_map" in value:
        import aws_sdk_quicksight.types.logical_table_map

        out["LogicalTableMap"] = (
            aws_sdk_quicksight.types.logical_table_map.serialize_json(
                value["logical_table_map"]
            )
        )
    import aws_sdk_quicksight.types.data_set_import_mode

    out["ImportMode"] = aws_sdk_quicksight.types.data_set_import_mode.serialize_json(
        value["import_mode"]
    )
    if "column_groups" in value:
        import aws_sdk_quicksight.types.column_group_list

        out["ColumnGroups"] = aws_sdk_quicksight.types.column_group_list.serialize_json(
            value["column_groups"]
        )
    if "field_folders" in value:
        import aws_sdk_quicksight.types.field_folder_map

        out["FieldFolders"] = aws_sdk_quicksight.types.field_folder_map.serialize_json(
            value["field_folders"]
        )
    if "row_level_permission_data_set" in value:
        import aws_sdk_quicksight.types.row_level_permission_data_set

        out["RowLevelPermissionDataSet"] = (
            aws_sdk_quicksight.types.row_level_permission_data_set.serialize_json(
                value["row_level_permission_data_set"]
            )
        )
    if "row_level_permission_tag_configuration" in value:
        import aws_sdk_quicksight.types.row_level_permission_tag_configuration

        out["RowLevelPermissionTagConfiguration"] = (
            aws_sdk_quicksight.types.row_level_permission_tag_configuration.serialize_json(
                value["row_level_permission_tag_configuration"]
            )
        )
    if "column_level_permission_rules" in value:
        import aws_sdk_quicksight.types.column_level_permission_rule_list

        out["ColumnLevelPermissionRules"] = (
            aws_sdk_quicksight.types.column_level_permission_rule_list.serialize_json(
                value["column_level_permission_rules"]
            )
        )
    if "data_set_usage_configuration" in value:
        import aws_sdk_quicksight.types.data_set_usage_configuration

        out["DataSetUsageConfiguration"] = (
            aws_sdk_quicksight.types.data_set_usage_configuration.serialize_json(
                value["data_set_usage_configuration"]
            )
        )
    if "dataset_parameters" in value:
        import aws_sdk_quicksight.types.dataset_parameter_list

        out["DatasetParameters"] = (
            aws_sdk_quicksight.types.dataset_parameter_list.serialize_json(
                value["dataset_parameters"]
            )
        )
    if "performance_configuration" in value:
        import aws_sdk_quicksight.types.performance_configuration

        out["PerformanceConfiguration"] = (
            aws_sdk_quicksight.types.performance_configuration.serialize_json(
                value["performance_configuration"]
            )
        )
    if "data_prep_configuration" in value:
        import aws_sdk_quicksight.types.data_prep_configuration

        out["DataPrepConfiguration"] = (
            aws_sdk_quicksight.types.data_prep_configuration.serialize_json(
                value["data_prep_configuration"]
            )
        )
    if "semantic_model_configuration" in value:
        import aws_sdk_quicksight.types.semantic_model_configuration

        out["SemanticModelConfiguration"] = (
            aws_sdk_quicksight.types.semantic_model_configuration.serialize_json(
                value["semantic_model_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDataSetRequest:
    out: UpdateDataSetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDataSetRequest.name required")
    if "PhysicalTableMap" in data:
        import aws_sdk_quicksight.types.physical_table_map

        out["physical_table_map"] = (
            aws_sdk_quicksight.types.physical_table_map.deserialize_json(
                data["PhysicalTableMap"]
            )
        )
    else:
        raise DeserializationError("UpdateDataSetRequest.physical_table_map required")
    if "LogicalTableMap" in data:
        import aws_sdk_quicksight.types.logical_table_map

        out["logical_table_map"] = (
            aws_sdk_quicksight.types.logical_table_map.deserialize_json(
                data["LogicalTableMap"]
            )
        )
    if "ImportMode" in data:
        import aws_sdk_quicksight.types.data_set_import_mode

        out["import_mode"] = (
            aws_sdk_quicksight.types.data_set_import_mode.deserialize_json(
                data["ImportMode"]
            )
        )
    else:
        raise DeserializationError("UpdateDataSetRequest.import_mode required")
    if "ColumnGroups" in data:
        import aws_sdk_quicksight.types.column_group_list

        out["column_groups"] = (
            aws_sdk_quicksight.types.column_group_list.deserialize_json(
                data["ColumnGroups"]
            )
        )
    if "FieldFolders" in data:
        import aws_sdk_quicksight.types.field_folder_map

        out["field_folders"] = (
            aws_sdk_quicksight.types.field_folder_map.deserialize_json(
                data["FieldFolders"]
            )
        )
    if "RowLevelPermissionDataSet" in data:
        import aws_sdk_quicksight.types.row_level_permission_data_set

        out["row_level_permission_data_set"] = (
            aws_sdk_quicksight.types.row_level_permission_data_set.deserialize_json(
                data["RowLevelPermissionDataSet"]
            )
        )
    if "RowLevelPermissionTagConfiguration" in data:
        import aws_sdk_quicksight.types.row_level_permission_tag_configuration

        out["row_level_permission_tag_configuration"] = (
            aws_sdk_quicksight.types.row_level_permission_tag_configuration.deserialize_json(
                data["RowLevelPermissionTagConfiguration"]
            )
        )
    if "ColumnLevelPermissionRules" in data:
        import aws_sdk_quicksight.types.column_level_permission_rule_list

        out["column_level_permission_rules"] = (
            aws_sdk_quicksight.types.column_level_permission_rule_list.deserialize_json(
                data["ColumnLevelPermissionRules"]
            )
        )
    if "DataSetUsageConfiguration" in data:
        import aws_sdk_quicksight.types.data_set_usage_configuration

        out["data_set_usage_configuration"] = (
            aws_sdk_quicksight.types.data_set_usage_configuration.deserialize_json(
                data["DataSetUsageConfiguration"]
            )
        )
    if "DatasetParameters" in data:
        import aws_sdk_quicksight.types.dataset_parameter_list

        out["dataset_parameters"] = (
            aws_sdk_quicksight.types.dataset_parameter_list.deserialize_json(
                data["DatasetParameters"]
            )
        )
    if "PerformanceConfiguration" in data:
        import aws_sdk_quicksight.types.performance_configuration

        out["performance_configuration"] = (
            aws_sdk_quicksight.types.performance_configuration.deserialize_json(
                data["PerformanceConfiguration"]
            )
        )
    if "DataPrepConfiguration" in data:
        import aws_sdk_quicksight.types.data_prep_configuration

        out["data_prep_configuration"] = (
            aws_sdk_quicksight.types.data_prep_configuration.deserialize_json(
                data["DataPrepConfiguration"]
            )
        )
    if "SemanticModelConfiguration" in data:
        import aws_sdk_quicksight.types.semantic_model_configuration

        out["semantic_model_configuration"] = (
            aws_sdk_quicksight.types.semantic_model_configuration.deserialize_json(
                data["SemanticModelConfiguration"]
            )
        )
    return out
