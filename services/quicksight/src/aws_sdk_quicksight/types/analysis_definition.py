"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.analysis_defaults
    import aws_sdk_quicksight.types.asset_options
    import aws_sdk_quicksight.types.calculated_fields
    import aws_sdk_quicksight.types.column_configuration_list
    import aws_sdk_quicksight.types.data_set_identifier_declaration_list
    import aws_sdk_quicksight.types.filter_group_list
    import aws_sdk_quicksight.types.parameter_declaration_list
    import aws_sdk_quicksight.types.query_execution_options
    import aws_sdk_quicksight.types.sheet_definition_list
    import aws_sdk_quicksight.types.static_file_list
    import aws_sdk_quicksight.types.tooltip_sheet_definition_list


class AnalysisDefinition(TypedDict):
    data_set_identifier_declarations: "aws_sdk_quicksight.types.data_set_identifier_declaration_list.DataSetIdentifierDeclarationList"
    """<p>An array of dataset identifier declarations. This mapping allows the usage of dataset identifiers instead of dataset ARNs throughout analysis sub-structures.</p>"""
    sheets: NotRequired[
        "aws_sdk_quicksight.types.sheet_definition_list.SheetDefinitionList"
    ]
    """<p>An array of sheet definitions for an analysis. Each <code>SheetDefinition</code> provides detailed information about a sheet within this analysis.</p>"""
    tooltip_sheets: NotRequired[
        "aws_sdk_quicksight.types.tooltip_sheet_definition_list.TooltipSheetDefinitionList"
    ]
    """<p>An array of tooltip sheet definitions for an analysis. Each <code>TooltipSheetDefinition</code> provides detailed information about a tooltip sheet within this analysis.</p>"""
    calculated_fields: NotRequired[
        "aws_sdk_quicksight.types.calculated_fields.CalculatedFields"
    ]
    """<p>An array of calculated field definitions for the analysis.</p>"""
    parameter_declarations: NotRequired[
        "aws_sdk_quicksight.types.parameter_declaration_list.ParameterDeclarationList"
    ]
    r"""<p>An array of parameter declarations for an analysis.</p> <p>Parameters are named variables that can transfer a value for use by an action or an object.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-quicksight.html\">Parameters in Amazon Quick Sight</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    filter_groups: NotRequired[
        "aws_sdk_quicksight.types.filter_group_list.FilterGroupList"
    ]
    r"""<p>Filter definitions for an analysis.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/adding-a-filter.html\">Filtering Data in Amazon Quick Sight</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    column_configurations: NotRequired[
        "aws_sdk_quicksight.types.column_configuration_list.ColumnConfigurationList"
    ]
    """<p> An array of analysis-level column configurations. Column configurations can be used to set default formatting for a column to be used throughout an analysis. </p>"""
    analysis_defaults: NotRequired[
        "aws_sdk_quicksight.types.analysis_defaults.AnalysisDefaults"
    ]
    options: NotRequired["aws_sdk_quicksight.types.asset_options.AssetOptions"]
    """<p>An array of option definitions for an analysis.</p>"""
    query_execution_options: NotRequired[
        "aws_sdk_quicksight.types.query_execution_options.QueryExecutionOptions"
    ]
    static_files: NotRequired[
        "aws_sdk_quicksight.types.static_file_list.StaticFileList"
    ]
    """<p>The static files for the definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisDefinition) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.data_set_identifier_declaration_list

    out["DataSetIdentifierDeclarations"] = (
        aws_sdk_quicksight.types.data_set_identifier_declaration_list.serialize_json(
            value["data_set_identifier_declarations"]
        )
    )
    if "sheets" in value:
        import aws_sdk_quicksight.types.sheet_definition_list

        out["Sheets"] = aws_sdk_quicksight.types.sheet_definition_list.serialize_json(
            value["sheets"]
        )
    if "tooltip_sheets" in value:
        import aws_sdk_quicksight.types.tooltip_sheet_definition_list

        out["TooltipSheets"] = (
            aws_sdk_quicksight.types.tooltip_sheet_definition_list.serialize_json(
                value["tooltip_sheets"]
            )
        )
    if "calculated_fields" in value:
        import aws_sdk_quicksight.types.calculated_fields

        out["CalculatedFields"] = (
            aws_sdk_quicksight.types.calculated_fields.serialize_json(
                value["calculated_fields"]
            )
        )
    if "parameter_declarations" in value:
        import aws_sdk_quicksight.types.parameter_declaration_list

        out["ParameterDeclarations"] = (
            aws_sdk_quicksight.types.parameter_declaration_list.serialize_json(
                value["parameter_declarations"]
            )
        )
    if "filter_groups" in value:
        import aws_sdk_quicksight.types.filter_group_list

        out["FilterGroups"] = aws_sdk_quicksight.types.filter_group_list.serialize_json(
            value["filter_groups"]
        )
    if "column_configurations" in value:
        import aws_sdk_quicksight.types.column_configuration_list

        out["ColumnConfigurations"] = (
            aws_sdk_quicksight.types.column_configuration_list.serialize_json(
                value["column_configurations"]
            )
        )
    if "analysis_defaults" in value:
        import aws_sdk_quicksight.types.analysis_defaults

        out["AnalysisDefaults"] = (
            aws_sdk_quicksight.types.analysis_defaults.serialize_json(
                value["analysis_defaults"]
            )
        )
    if "options" in value:
        import aws_sdk_quicksight.types.asset_options

        out["Options"] = aws_sdk_quicksight.types.asset_options.serialize_json(
            value["options"]
        )
    if "query_execution_options" in value:
        import aws_sdk_quicksight.types.query_execution_options

        out["QueryExecutionOptions"] = (
            aws_sdk_quicksight.types.query_execution_options.serialize_json(
                value["query_execution_options"]
            )
        )
    if "static_files" in value:
        import aws_sdk_quicksight.types.static_file_list

        out["StaticFiles"] = aws_sdk_quicksight.types.static_file_list.serialize_json(
            value["static_files"]
        )
    return out


def deserialize_json(data: dict) -> AnalysisDefinition:
    out: AnalysisDefinition = {}  # type: ignore[typeddict-item]
    if "DataSetIdentifierDeclarations" in data:
        import aws_sdk_quicksight.types.data_set_identifier_declaration_list

        out["data_set_identifier_declarations"] = (
            aws_sdk_quicksight.types.data_set_identifier_declaration_list.deserialize_json(
                data["DataSetIdentifierDeclarations"]
            )
        )
    else:
        raise DeserializationError(
            "AnalysisDefinition.data_set_identifier_declarations required"
        )
    if "Sheets" in data:
        import aws_sdk_quicksight.types.sheet_definition_list

        out["sheets"] = aws_sdk_quicksight.types.sheet_definition_list.deserialize_json(
            data["Sheets"]
        )
    if "TooltipSheets" in data:
        import aws_sdk_quicksight.types.tooltip_sheet_definition_list

        out["tooltip_sheets"] = (
            aws_sdk_quicksight.types.tooltip_sheet_definition_list.deserialize_json(
                data["TooltipSheets"]
            )
        )
    if "CalculatedFields" in data:
        import aws_sdk_quicksight.types.calculated_fields

        out["calculated_fields"] = (
            aws_sdk_quicksight.types.calculated_fields.deserialize_json(
                data["CalculatedFields"]
            )
        )
    if "ParameterDeclarations" in data:
        import aws_sdk_quicksight.types.parameter_declaration_list

        out["parameter_declarations"] = (
            aws_sdk_quicksight.types.parameter_declaration_list.deserialize_json(
                data["ParameterDeclarations"]
            )
        )
    if "FilterGroups" in data:
        import aws_sdk_quicksight.types.filter_group_list

        out["filter_groups"] = (
            aws_sdk_quicksight.types.filter_group_list.deserialize_json(
                data["FilterGroups"]
            )
        )
    if "ColumnConfigurations" in data:
        import aws_sdk_quicksight.types.column_configuration_list

        out["column_configurations"] = (
            aws_sdk_quicksight.types.column_configuration_list.deserialize_json(
                data["ColumnConfigurations"]
            )
        )
    if "AnalysisDefaults" in data:
        import aws_sdk_quicksight.types.analysis_defaults

        out["analysis_defaults"] = (
            aws_sdk_quicksight.types.analysis_defaults.deserialize_json(
                data["AnalysisDefaults"]
            )
        )
    if "Options" in data:
        import aws_sdk_quicksight.types.asset_options

        out["options"] = aws_sdk_quicksight.types.asset_options.deserialize_json(
            data["Options"]
        )
    if "QueryExecutionOptions" in data:
        import aws_sdk_quicksight.types.query_execution_options

        out["query_execution_options"] = (
            aws_sdk_quicksight.types.query_execution_options.deserialize_json(
                data["QueryExecutionOptions"]
            )
        )
    if "StaticFiles" in data:
        import aws_sdk_quicksight.types.static_file_list

        out["static_files"] = (
            aws_sdk_quicksight.types.static_file_list.deserialize_json(
                data["StaticFiles"]
            )
        )
    return out
