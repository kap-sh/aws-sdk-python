"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryFilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.custom_filter_configuration
    import aws_sdk_quicksight.types.custom_filter_list_configuration
    import aws_sdk_quicksight.types.filter_list_configuration


class CategoryFilterConfiguration(TypedDict, closed=True):
    filter_list_configuration: NotRequired[
        "aws_sdk_quicksight.types.filter_list_configuration.FilterListConfiguration"
    ]
    """<p>A list of filter configurations. In the Quick Sight console, this filter type is called a filter list.</p>"""
    custom_filter_list_configuration: NotRequired[
        "aws_sdk_quicksight.types.custom_filter_list_configuration.CustomFilterListConfiguration"
    ]
    """<p>A list of custom filter values. In the Quick Sight console, this filter type is called a custom filter list.</p>"""
    custom_filter_configuration: NotRequired[
        "aws_sdk_quicksight.types.custom_filter_configuration.CustomFilterConfiguration"
    ]
    """<p>A custom filter that filters based on a single value. This filter can be partially matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryFilterConfiguration) -> dict:
    out: dict = {}
    if "filter_list_configuration" in value:
        import aws_sdk_quicksight.types.filter_list_configuration

        out["FilterListConfiguration"] = (
            aws_sdk_quicksight.types.filter_list_configuration.serialize_json(
                value["filter_list_configuration"]
            )
        )
    if "custom_filter_list_configuration" in value:
        import aws_sdk_quicksight.types.custom_filter_list_configuration

        out["CustomFilterListConfiguration"] = (
            aws_sdk_quicksight.types.custom_filter_list_configuration.serialize_json(
                value["custom_filter_list_configuration"]
            )
        )
    if "custom_filter_configuration" in value:
        import aws_sdk_quicksight.types.custom_filter_configuration

        out["CustomFilterConfiguration"] = (
            aws_sdk_quicksight.types.custom_filter_configuration.serialize_json(
                value["custom_filter_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CategoryFilterConfiguration:
    out: CategoryFilterConfiguration = {}  # type: ignore[typeddict-item]
    if "FilterListConfiguration" in data:
        import aws_sdk_quicksight.types.filter_list_configuration

        out["filter_list_configuration"] = (
            aws_sdk_quicksight.types.filter_list_configuration.deserialize_json(
                data["FilterListConfiguration"]
            )
        )
    if "CustomFilterListConfiguration" in data:
        import aws_sdk_quicksight.types.custom_filter_list_configuration

        out["custom_filter_list_configuration"] = (
            aws_sdk_quicksight.types.custom_filter_list_configuration.deserialize_json(
                data["CustomFilterListConfiguration"]
            )
        )
    if "CustomFilterConfiguration" in data:
        import aws_sdk_quicksight.types.custom_filter_configuration

        out["custom_filter_configuration"] = (
            aws_sdk_quicksight.types.custom_filter_configuration.deserialize_json(
                data["CustomFilterConfiguration"]
            )
        )
    return out
