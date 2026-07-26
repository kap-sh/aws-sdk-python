"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.boolean_operator
    import capo_sagemaker.types.filter_list
    import capo_sagemaker.types.nested_filters_list
    import capo_sagemaker.types.search_expression_list


class SearchExpression(TypedDict, closed=True):
    filters: NotRequired["capo_sagemaker.types.filter_list.FilterList"]
    """<p>A list of filter objects.</p>"""
    nested_filters: NotRequired[
        "capo_sagemaker.types.nested_filters_list.NestedFiltersList"
    ]
    """<p>A list of nested filter objects.</p>"""
    sub_expressions: NotRequired[
        "capo_sagemaker.types.search_expression_list.SearchExpressionList"
    ]
    """<p>A list of search expression objects.</p>"""
    operator: NotRequired["capo_sagemaker.types.boolean_operator.BooleanOperator"]
    """<p>A Boolean operator used to evaluate the search expression. If you want every conditional statement in all lists to be satisfied for the entire search expression to be true, specify <code>And</code>. If only a single conditional statement needs to be true for the entire search expression to be true, specify <code>Or</code>. The default value is <code>And</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchExpression) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_sagemaker.types.filter_list

        out["Filters"] = capo_sagemaker.types.filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "nested_filters" in value:
        import capo_sagemaker.types.nested_filters_list

        out["NestedFilters"] = (
            capo_sagemaker.types.nested_filters_list.serialize_aws_json_1_1(
                value["nested_filters"]
            )
        )
    if "sub_expressions" in value:
        import capo_sagemaker.types.search_expression_list

        out["SubExpressions"] = (
            capo_sagemaker.types.search_expression_list.serialize_aws_json_1_1(
                value["sub_expressions"]
            )
        )
    if "operator" in value:
        import capo_sagemaker.types.boolean_operator

        out["Operator"] = capo_sagemaker.types.boolean_operator.serialize_aws_json_1_1(
            value["operator"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchExpression:
    out: SearchExpression = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import capo_sagemaker.types.filter_list

        out["filters"] = capo_sagemaker.types.filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "NestedFilters" in data:
        import capo_sagemaker.types.nested_filters_list

        out["nested_filters"] = (
            capo_sagemaker.types.nested_filters_list.deserialize_aws_json_1_1(
                data["NestedFilters"]
            )
        )
    if "SubExpressions" in data:
        import capo_sagemaker.types.search_expression_list

        out["sub_expressions"] = (
            capo_sagemaker.types.search_expression_list.deserialize_aws_json_1_1(
                data["SubExpressions"]
            )
        )
    if "Operator" in data:
        import capo_sagemaker.types.boolean_operator

        out["operator"] = (
            capo_sagemaker.types.boolean_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    return out
