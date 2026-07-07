"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryInnerFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.category_filter_configuration
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.default_filter_control_configuration


class CategoryInnerFilter(TypedDict, closed=True):
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    configuration: "aws_sdk_quicksight.types.category_filter_configuration.CategoryFilterConfiguration"
    default_filter_control_configuration: NotRequired[
        "aws_sdk_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryInnerFilter) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> CategoryInnerFilter:
    out: CategoryInnerFilter = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("CategoryInnerFilter.column required")
    if "Configuration" in data:
        import aws_sdk_quicksight.types.category_filter_configuration

        out["configuration"] = (
            aws_sdk_quicksight.types.category_filter_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("CategoryInnerFilter.configuration required")
    if "DefaultFilterControlConfiguration" in data:
        import aws_sdk_quicksight.types.default_filter_control_configuration

        out["default_filter_control_configuration"] = (
            aws_sdk_quicksight.types.default_filter_control_configuration.deserialize_json(
                data["DefaultFilterControlConfiguration"]
            )
        )
    return out
