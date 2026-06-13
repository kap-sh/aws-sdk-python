"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomFilterListConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.category_filter_match_operator
    import aws_sdk_quicksight.types.category_filter_select_all_options
    import aws_sdk_quicksight.types.category_value_list
    import aws_sdk_quicksight.types.filter_null_option


class CustomFilterListConfiguration(TypedDict):
    match_operator: "aws_sdk_quicksight.types.category_filter_match_operator.CategoryFilterMatchOperator"
    """<p>The match operator that is used to determine if a filter should be applied.</p>"""
    category_values: NotRequired[
        "aws_sdk_quicksight.types.category_value_list.CategoryValueList"
    ]
    """<p>The list of category values for the filter.</p>"""
    select_all_options: NotRequired[
        "aws_sdk_quicksight.types.category_filter_select_all_options.CategoryFilterSelectAllOptions"
    ]
    """<p>Select all of the values. Null is not the assigned value of select all.</p> <ul> <li> <p> <code>FILTER_ALL_VALUES</code> </p> </li> </ul>"""
    null_option: "aws_sdk_quicksight.types.filter_null_option.FilterNullOption"
    """<p>This option determines how null values should be treated when filtering data.</p> <ul> <li> <p> <code>ALL_VALUES</code>: Include null values in filtered results.</p> </li> <li> <p> <code>NULLS_ONLY</code>: Only include null values in filtered results.</p> </li> <li> <p> <code>NON_NULLS_ONLY</code>: Exclude null values from filtered results.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomFilterListConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.category_filter_match_operator

    out["MatchOperator"] = (
        aws_sdk_quicksight.types.category_filter_match_operator.serialize_json(
            value["match_operator"]
        )
    )
    if "category_values" in value:
        import aws_sdk_quicksight.types.category_value_list

        out["CategoryValues"] = (
            aws_sdk_quicksight.types.category_value_list.serialize_json(
                value["category_values"]
            )
        )
    if "select_all_options" in value:
        import aws_sdk_quicksight.types.category_filter_select_all_options

        out["SelectAllOptions"] = (
            aws_sdk_quicksight.types.category_filter_select_all_options.serialize_json(
                value["select_all_options"]
            )
        )
    import aws_sdk_quicksight.types.filter_null_option

    out["NullOption"] = aws_sdk_quicksight.types.filter_null_option.serialize_json(
        value["null_option"]
    )
    return out


def deserialize_json(data: dict) -> CustomFilterListConfiguration:
    out: CustomFilterListConfiguration = {}  # type: ignore[typeddict-item]
    if "MatchOperator" in data:
        import aws_sdk_quicksight.types.category_filter_match_operator

        out["match_operator"] = (
            aws_sdk_quicksight.types.category_filter_match_operator.deserialize_json(
                data["MatchOperator"]
            )
        )
    else:
        raise DeserializationError(
            "CustomFilterListConfiguration.match_operator required"
        )
    if "CategoryValues" in data:
        import aws_sdk_quicksight.types.category_value_list

        out["category_values"] = (
            aws_sdk_quicksight.types.category_value_list.deserialize_json(
                data["CategoryValues"]
            )
        )
    if "SelectAllOptions" in data:
        import aws_sdk_quicksight.types.category_filter_select_all_options

        out["select_all_options"] = (
            aws_sdk_quicksight.types.category_filter_select_all_options.deserialize_json(
                data["SelectAllOptions"]
            )
        )
    if "NullOption" in data:
        import aws_sdk_quicksight.types.filter_null_option

        out["null_option"] = (
            aws_sdk_quicksight.types.filter_null_option.deserialize_json(
                data["NullOption"]
            )
        )
    else:
        raise DeserializationError("CustomFilterListConfiguration.null_option required")
    return out
