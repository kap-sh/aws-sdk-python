"""Generated from Smithy shape ``com.amazonaws.inspector2#LambdaFunctionAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.lambda_function_sort_by
    import aws_sdk_inspector2.types.map_filter_list
    import aws_sdk_inspector2.types.sort_order
    import aws_sdk_inspector2.types.string_filter_list


class LambdaFunctionAggregation(TypedDict):
    resource_ids: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The resource IDs to include in the aggregation results.</p>"""
    function_names: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The Amazon Web Services Lambda function names to include in the aggregation results.</p>"""
    runtimes: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Returns findings aggregated by Amazon Web Services Lambda function runtime environments.</p>"""
    function_tags: NotRequired["aws_sdk_inspector2.types.map_filter_list.MapFilterList"]
    """<p>The tags to include in the aggregation results.</p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.sort_order.SortOrder"]
    """<p>The order to use for sorting the results.</p>"""
    sort_by: NotRequired[
        "aws_sdk_inspector2.types.lambda_function_sort_by.LambdaFunctionSortBy"
    ]
    """<p>The finding severity to use for sorting the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaFunctionAggregation) -> dict:
    out: dict = {}
    if "resource_ids" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["resourceIds"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["resource_ids"]
        )
    if "function_names" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["functionNames"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["function_names"]
            )
        )
    if "runtimes" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["runtimes"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["runtimes"]
        )
    if "function_tags" in value:
        import aws_sdk_inspector2.types.map_filter_list

        out["functionTags"] = aws_sdk_inspector2.types.map_filter_list.serialize_json(
            value["function_tags"]
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    return out


def deserialize_json(data: dict) -> LambdaFunctionAggregation:
    out: LambdaFunctionAggregation = {}  # type: ignore[typeddict-item]
    if "resourceIds" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["resource_ids"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["resourceIds"]
            )
        )
    if "functionNames" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["function_names"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["functionNames"]
            )
        )
    if "runtimes" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["runtimes"] = aws_sdk_inspector2.types.string_filter_list.deserialize_json(
            data["runtimes"]
        )
    if "functionTags" in data:
        import aws_sdk_inspector2.types.map_filter_list

        out["function_tags"] = (
            aws_sdk_inspector2.types.map_filter_list.deserialize_json(
                data["functionTags"]
            )
        )
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    return out
