"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.category_filter_configuration
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.default_filter_control_configuration
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class CategoryFilter(TypedDict):
    filter_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    configuration: "aws_sdk_quicksight.types.category_filter_configuration.CategoryFilterConfiguration"
    """<p>The configuration for a <code>CategoryFilter</code>.</p>"""
    default_filter_control_configuration: NotRequired[
        "aws_sdk_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    import aws_sdk_quicksight.types.category_filter_configuration

    out["Configuration"] = (
        aws_sdk_quicksight.types.category_filter_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "default_filter_control_configuration" in value:
        import aws_sdk_quicksight.types.default_filter_control_configuration

        out["DefaultFilterControlConfiguration"] = (
            aws_sdk_quicksight.types.default_filter_control_configuration.serialize_json(
                value["default_filter_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CategoryFilter:
    out: CategoryFilter = {}  # type: ignore[typeddict-item]
    if "FilterId" in data:
        out["filter_id"] = data["FilterId"]
    else:
        raise DeserializationError("CategoryFilter.filter_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("CategoryFilter.column required")
    if "Configuration" in data:
        import aws_sdk_quicksight.types.category_filter_configuration

        out["configuration"] = (
            aws_sdk_quicksight.types.category_filter_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("CategoryFilter.configuration required")
    if "DefaultFilterControlConfiguration" in data:
        import aws_sdk_quicksight.types.default_filter_control_configuration

        out["default_filter_control_configuration"] = (
            aws_sdk_quicksight.types.default_filter_control_configuration.deserialize_json(
                data["DefaultFilterControlConfiguration"]
            )
        )
    return out
