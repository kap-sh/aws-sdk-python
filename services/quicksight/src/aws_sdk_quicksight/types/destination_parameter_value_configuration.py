"""Generated from Smithy shape ``com.amazonaws.quicksight#DestinationParameterValueConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.custom_values_configuration
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.select_all_value_options
    import aws_sdk_quicksight.types.string


class DestinationParameterValueConfiguration(TypedDict, closed=True):
    custom_values_configuration: NotRequired[
        "aws_sdk_quicksight.types.custom_values_configuration.CustomValuesConfiguration"
    ]
    """<p>The configuration of custom values for destination parameter in <code>DestinationParameterValueConfiguration</code>.</p>"""
    select_all_value_options: NotRequired[
        "aws_sdk_quicksight.types.select_all_value_options.SelectAllValueOptions"
    ]
    """<p>The configuration that selects all options.</p>"""
    source_parameter_name: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The source parameter name of the destination parameter.</p>"""
    source_field: NotRequired["aws_sdk_quicksight.types.field_id.FieldId"]
    """<p>The source field ID of the destination parameter.</p>"""
    source_column: NotRequired[
        "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationParameterValueConfiguration) -> dict:
    out: dict = {}
    if "custom_values_configuration" in value:
        import aws_sdk_quicksight.types.custom_values_configuration

        out["CustomValuesConfiguration"] = (
            aws_sdk_quicksight.types.custom_values_configuration.serialize_json(
                value["custom_values_configuration"]
            )
        )
    if "select_all_value_options" in value:
        import aws_sdk_quicksight.types.select_all_value_options

        out["SelectAllValueOptions"] = (
            aws_sdk_quicksight.types.select_all_value_options.serialize_json(
                value["select_all_value_options"]
            )
        )
    if "source_parameter_name" in value:
        out["SourceParameterName"] = value["source_parameter_name"]
    if "source_field" in value:
        out["SourceField"] = value["source_field"]
    if "source_column" in value:
        import aws_sdk_quicksight.types.column_identifier

        out["SourceColumn"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
            value["source_column"]
        )
    return out


def deserialize_json(data: dict) -> DestinationParameterValueConfiguration:
    out: DestinationParameterValueConfiguration = {}  # type: ignore[typeddict-item]
    if "CustomValuesConfiguration" in data:
        import aws_sdk_quicksight.types.custom_values_configuration

        out["custom_values_configuration"] = (
            aws_sdk_quicksight.types.custom_values_configuration.deserialize_json(
                data["CustomValuesConfiguration"]
            )
        )
    if "SelectAllValueOptions" in data:
        import aws_sdk_quicksight.types.select_all_value_options

        out["select_all_value_options"] = (
            aws_sdk_quicksight.types.select_all_value_options.deserialize_json(
                data["SelectAllValueOptions"]
            )
        )
    if "SourceParameterName" in data:
        out["source_parameter_name"] = data["SourceParameterName"]
    if "SourceField" in data:
        out["source_field"] = data["SourceField"]
    if "SourceColumn" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["source_column"] = (
            aws_sdk_quicksight.types.column_identifier.deserialize_json(
                data["SourceColumn"]
            )
        )
    return out
