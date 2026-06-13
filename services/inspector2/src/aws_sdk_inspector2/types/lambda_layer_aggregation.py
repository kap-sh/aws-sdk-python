"""Generated from Smithy shape ``com.amazonaws.inspector2#LambdaLayerAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.lambda_layer_sort_by
    import aws_sdk_inspector2.types.sort_order
    import aws_sdk_inspector2.types.string_filter_list


class LambdaLayerAggregation(TypedDict):
    function_names: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The names of the Amazon Web Services Lambda functions associated with the layers.</p>"""
    resource_ids: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The resource IDs for the Amazon Web Services Lambda function layers.</p>"""
    layer_arns: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Lambda function layer. </p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.sort_order.SortOrder"]
    """<p>The order to use for sorting the results.</p>"""
    sort_by: NotRequired[
        "aws_sdk_inspector2.types.lambda_layer_sort_by.LambdaLayerSortBy"
    ]
    """<p>The finding severity to use for sorting the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaLayerAggregation) -> dict:
    out: dict = {}
    if "function_names" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["functionNames"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["function_names"]
            )
        )
    if "resource_ids" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["resourceIds"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["resource_ids"]
        )
    if "layer_arns" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["layerArns"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["layer_arns"]
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    return out


def deserialize_json(data: dict) -> LambdaLayerAggregation:
    out: LambdaLayerAggregation = {}  # type: ignore[typeddict-item]
    if "functionNames" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["function_names"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["functionNames"]
            )
        )
    if "resourceIds" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["resource_ids"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["resourceIds"]
            )
        )
    if "layerArns" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["layer_arns"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["layerArns"]
            )
        )
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    return out
