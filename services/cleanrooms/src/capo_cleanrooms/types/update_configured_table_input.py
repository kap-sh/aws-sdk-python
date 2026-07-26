"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateConfiguredTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.allowed_column_list
    import capo_cleanrooms.types.analysis_method
    import capo_cleanrooms.types.configured_table_identifier
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.selected_analysis_methods
    import capo_cleanrooms.types.table_description
    import capo_cleanrooms.types.table_reference


class UpdateConfiguredTableInput(TypedDict, closed=True):
    configured_table_identifier: (
        "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier"
    )
    """<p>The identifier for the configured table to update. Currently accepts the configured table ID.</p>"""
    name: NotRequired["capo_cleanrooms.types.display_name.DisplayName"]
    """<p>A new name for the configured table.</p>"""
    description: NotRequired["capo_cleanrooms.types.table_description.TableDescription"]
    """<p>A new description for the configured table.</p>"""
    table_reference: NotRequired["capo_cleanrooms.types.table_reference.TableReference"]
    allowed_columns: NotRequired[
        "capo_cleanrooms.types.allowed_column_list.AllowedColumnList"
    ]
    """<p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>"""
    analysis_method: NotRequired["capo_cleanrooms.types.analysis_method.AnalysisMethod"]
    """<p> The analysis method for the configured table.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>"""
    selected_analysis_methods: NotRequired[
        "capo_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
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
        import capo_cleanrooms.types.table_reference

        out["tableReference"] = capo_cleanrooms.types.table_reference.serialize_json(
            value["table_reference"]
        )
    if "allowed_columns" in value:
        import capo_cleanrooms.types.allowed_column_list

        out["allowedColumns"] = (
            capo_cleanrooms.types.allowed_column_list.serialize_json(
                value["allowed_columns"]
            )
        )
    if "analysis_method" in value:
        import capo_cleanrooms.types.analysis_method

        out["analysisMethod"] = capo_cleanrooms.types.analysis_method.serialize_json(
            value["analysis_method"]
        )
    if "selected_analysis_methods" in value:
        import capo_cleanrooms.types.selected_analysis_methods

        out["selectedAnalysisMethods"] = (
            capo_cleanrooms.types.selected_analysis_methods.serialize_json(
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
        import capo_cleanrooms.types.table_reference

        out["table_reference"] = capo_cleanrooms.types.table_reference.deserialize_json(
            data["tableReference"]
        )
    if "allowedColumns" in data:
        import capo_cleanrooms.types.allowed_column_list

        out["allowed_columns"] = (
            capo_cleanrooms.types.allowed_column_list.deserialize_json(
                data["allowedColumns"]
            )
        )
    if "analysisMethod" in data:
        import capo_cleanrooms.types.analysis_method

        out["analysis_method"] = capo_cleanrooms.types.analysis_method.deserialize_json(
            data["analysisMethod"]
        )
    if "selectedAnalysisMethods" in data:
        import capo_cleanrooms.types.selected_analysis_methods

        out["selected_analysis_methods"] = (
            capo_cleanrooms.types.selected_analysis_methods.deserialize_json(
                data["selectedAnalysisMethods"]
            )
        )
    return out
