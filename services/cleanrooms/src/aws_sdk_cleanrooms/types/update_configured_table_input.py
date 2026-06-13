"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateConfiguredTableInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.allowed_column_list
    import aws_sdk_cleanrooms.types.analysis_method
    import aws_sdk_cleanrooms.types.configured_table_identifier
    import aws_sdk_cleanrooms.types.display_name
    import aws_sdk_cleanrooms.types.selected_analysis_methods
    import aws_sdk_cleanrooms.types.table_description
    import aws_sdk_cleanrooms.types.table_reference


class UpdateConfiguredTableInput(TypedDict):
    configured_table_identifier: (
        "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier"
    )
    """<p>The identifier for the configured table to update. Currently accepts the configured table ID.</p>"""
    name: NotRequired["aws_sdk_cleanrooms.types.display_name.DisplayName"]
    """<p>A new name for the configured table.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.table_description.TableDescription"
    ]
    """<p>A new description for the configured table.</p>"""
    table_reference: NotRequired[
        "aws_sdk_cleanrooms.types.table_reference.TableReference"
    ]
    allowed_columns: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_column_list.AllowedColumnList"
    ]
    """<p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>"""
    analysis_method: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_method.AnalysisMethod"
    ]
    """<p> The analysis method for the configured table.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>"""
    selected_analysis_methods: NotRequired[
        "aws_sdk_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
    ]
    """<p> The selected analysis methods for the table configuration update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredTableInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "table_reference" in value:
        import aws_sdk_cleanrooms.types.table_reference

        out["tableReference"] = aws_sdk_cleanrooms.types.table_reference.serialize_json(
            value["table_reference"]
        )
    if "allowed_columns" in value:
        import aws_sdk_cleanrooms.types.allowed_column_list

        out["allowedColumns"] = (
            aws_sdk_cleanrooms.types.allowed_column_list.serialize_json(
                value["allowed_columns"]
            )
        )
    if "analysis_method" in value:
        import aws_sdk_cleanrooms.types.analysis_method

        out["analysisMethod"] = aws_sdk_cleanrooms.types.analysis_method.serialize_json(
            value["analysis_method"]
        )
    if "selected_analysis_methods" in value:
        import aws_sdk_cleanrooms.types.selected_analysis_methods

        out["selectedAnalysisMethods"] = (
            aws_sdk_cleanrooms.types.selected_analysis_methods.serialize_json(
                value["selected_analysis_methods"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConfiguredTableInput:
    out: UpdateConfiguredTableInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "tableReference" in data:
        import aws_sdk_cleanrooms.types.table_reference

        out["table_reference"] = (
            aws_sdk_cleanrooms.types.table_reference.deserialize_json(
                data["tableReference"]
            )
        )
    if "allowedColumns" in data:
        import aws_sdk_cleanrooms.types.allowed_column_list

        out["allowed_columns"] = (
            aws_sdk_cleanrooms.types.allowed_column_list.deserialize_json(
                data["allowedColumns"]
            )
        )
    if "analysisMethod" in data:
        import aws_sdk_cleanrooms.types.analysis_method

        out["analysis_method"] = (
            aws_sdk_cleanrooms.types.analysis_method.deserialize_json(
                data["analysisMethod"]
            )
        )
    if "selectedAnalysisMethods" in data:
        import aws_sdk_cleanrooms.types.selected_analysis_methods

        out["selected_analysis_methods"] = (
            aws_sdk_cleanrooms.types.selected_analysis_methods.deserialize_json(
                data["selectedAnalysisMethods"]
            )
        )
    return out
