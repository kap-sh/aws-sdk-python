"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchExpression``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean_operator
    import aws_sdk_sagemaker.types.filter_list
    import aws_sdk_sagemaker.types.nested_filters_list
    import aws_sdk_sagemaker.types.search_expression_list


class SearchExpression(TypedDict):
    filters: NotRequired["aws_sdk_sagemaker.types.filter_list.FilterList"]
    """<p>A list of filter objects.</p>"""
    nested_filters: NotRequired[
        "aws_sdk_sagemaker.types.nested_filters_list.NestedFiltersList"
    ]
    """<p>A list of nested filter objects.</p>"""
    sub_expressions: NotRequired[
        "aws_sdk_sagemaker.types.search_expression_list.SearchExpressionList"
    ]
    """<p>A list of search expression objects.</p>"""
    operator: NotRequired["aws_sdk_sagemaker.types.boolean_operator.BooleanOperator"]
    """<p>A Boolean operator used to evaluate the search expression. If you want every conditional statement in all lists to be satisfied for the entire search expression to be true, specify <code>And</code>. If only a single conditional statement needs to be true for the entire search expression to be true, specify <code>Or</code>. The default value is <code>And</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchExpression) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_sagemaker.types.filter_list

        out["Filters"] = aws_sdk_sagemaker.types.filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "nested_filters" in value:
        import aws_sdk_sagemaker.types.nested_filters_list

        out["NestedFilters"] = (
            aws_sdk_sagemaker.types.nested_filters_list.serialize_aws_json_1_1(
                value["nested_filters"]
            )
        )
    if "sub_expressions" in value:
        import aws_sdk_sagemaker.types.search_expression_list

        out["SubExpressions"] = (
            aws_sdk_sagemaker.types.search_expression_list.serialize_aws_json_1_1(
                value["sub_expressions"]
            )
        )
    if "operator" in value:
        import aws_sdk_sagemaker.types.boolean_operator

        out["Operator"] = (
            aws_sdk_sagemaker.types.boolean_operator.serialize_aws_json_1_1(
                value["operator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchExpression:
    out: SearchExpression = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_sagemaker.types.filter_list

        out["filters"] = aws_sdk_sagemaker.types.filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "NestedFilters" in data:
        import aws_sdk_sagemaker.types.nested_filters_list

        out["nested_filters"] = (
            aws_sdk_sagemaker.types.nested_filters_list.deserialize_aws_json_1_1(
                data["NestedFilters"]
            )
        )
    if "SubExpressions" in data:
        import aws_sdk_sagemaker.types.search_expression_list

        out["sub_expressions"] = (
            aws_sdk_sagemaker.types.search_expression_list.deserialize_aws_json_1_1(
                data["SubExpressions"]
            )
        )
    if "Operator" in data:
        import aws_sdk_sagemaker.types.boolean_operator

        out["operator"] = (
            aws_sdk_sagemaker.types.boolean_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    return out
