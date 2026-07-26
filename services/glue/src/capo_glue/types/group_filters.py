"""Generated from Smithy shape ``com.amazonaws.glue#GroupFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.filter_expressions
    import capo_glue.types.filter_logical_operator
    import capo_glue.types.generic_limited_string


class GroupFilters(TypedDict, closed=True):
    group_name: "capo_glue.types.generic_limited_string.GenericLimitedString"
    """<p>The name of the filter group.</p>"""
    filters: "capo_glue.types.filter_expressions.FilterExpressions"
    """<p>A list of filter expressions that define the conditions for this group.</p>"""
    logical_operator: "capo_glue.types.filter_logical_operator.FilterLogicalOperator"
    """<p>The logical operator used to combine the filters in this group. Determines whether all filters must match (AND) or any filter can match (OR).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupFilters) -> dict:
    out: dict = {}
    out["GroupName"] = value["group_name"]
    import capo_glue.types.filter_expressions

    out["Filters"] = capo_glue.types.filter_expressions.serialize_aws_json_1_1(
        value["filters"]
    )
    import capo_glue.types.filter_logical_operator

    out["LogicalOperator"] = (
        capo_glue.types.filter_logical_operator.serialize_aws_json_1_1(
            value["logical_operator"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GroupFilters:
    out: GroupFilters = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    else:
        raise DeserializationError("GroupFilters.group_name required")
    if "Filters" in data:
        import capo_glue.types.filter_expressions

        out["filters"] = capo_glue.types.filter_expressions.deserialize_aws_json_1_1(
            data["Filters"]
        )
    else:
        raise DeserializationError("GroupFilters.filters required")
    if "LogicalOperator" in data:
        import capo_glue.types.filter_logical_operator

        out["logical_operator"] = (
            capo_glue.types.filter_logical_operator.deserialize_aws_json_1_1(
                data["LogicalOperator"]
            )
        )
    else:
        raise DeserializationError("GroupFilters.logical_operator required")
    return out
