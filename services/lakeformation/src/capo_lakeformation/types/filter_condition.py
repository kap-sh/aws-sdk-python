"""Generated from Smithy shape ``com.amazonaws.lakeformation#FilterCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.comparison_operator
    import capo_lakeformation.types.field_name_string
    import capo_lakeformation.types.string_value_list


class FilterCondition(TypedDict, closed=True):
    field: NotRequired["capo_lakeformation.types.field_name_string.FieldNameString"]
    """<p>The field to filter in the filter condition.</p>"""
    comparison_operator: NotRequired[
        "capo_lakeformation.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The comparison operator used in the filter condition.</p>"""
    string_value_list: NotRequired[
        "capo_lakeformation.types.string_value_list.StringValueList"
    ]
    """<p>A string with values used in evaluating the filter condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCondition) -> dict:
    out: dict = {}
    if "field" in value:
        import capo_lakeformation.types.field_name_string

        out["Field"] = capo_lakeformation.types.field_name_string.serialize_json(
            value["field"]
        )
    if "comparison_operator" in value:
        import capo_lakeformation.types.comparison_operator

        out["ComparisonOperator"] = (
            capo_lakeformation.types.comparison_operator.serialize_json(
                value["comparison_operator"]
            )
        )
    if "string_value_list" in value:
        import capo_lakeformation.types.string_value_list

        out["StringValueList"] = (
            capo_lakeformation.types.string_value_list.serialize_json(
                value["string_value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterCondition:
    out: FilterCondition = {}  # type: ignore[typeddict-item]
    if "Field" in data:
        import capo_lakeformation.types.field_name_string

        out["field"] = capo_lakeformation.types.field_name_string.deserialize_json(
            data["Field"]
        )
    if "ComparisonOperator" in data:
        import capo_lakeformation.types.comparison_operator

        out["comparison_operator"] = (
            capo_lakeformation.types.comparison_operator.deserialize_json(
                data["ComparisonOperator"]
            )
        )
    if "StringValueList" in data:
        import capo_lakeformation.types.string_value_list

        out["string_value_list"] = (
            capo_lakeformation.types.string_value_list.deserialize_json(
                data["StringValueList"]
            )
        )
    return out
