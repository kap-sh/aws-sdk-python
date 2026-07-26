"""Generated from Smithy shape ``com.amazonaws.inspector2#LambdaLayerAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.lambda_layer_sort_by
    import capo_inspector2.types.sort_order
    import capo_inspector2.types.string_filter_list


class LambdaLayerAggregation(TypedDict, closed=True):
    function_names: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The names of the Amazon Web Services Lambda functions associated with the layers.</p>"""
    resource_ids: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The resource IDs for the Amazon Web Services Lambda function layers.</p>"""
    layer_arns: NotRequired["capo_inspector2.types.string_filter_list.StringFilterList"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Lambda function layer. </p>"""
    sort_order: NotRequired["capo_inspector2.types.sort_order.SortOrder"]
    """<p>The order to use for sorting the results.</p>"""
    sort_by: NotRequired["capo_inspector2.types.lambda_layer_sort_by.LambdaLayerSortBy"]
    """<p>The finding severity to use for sorting the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaLayerAggregation) -> dict:
    out: dict = {}
    if "function_names" in value:
        import capo_inspector2.types.string_filter_list

        out["functionNames"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["function_names"]
        )
    if "resource_ids" in value:
        import capo_inspector2.types.string_filter_list

        out["resourceIds"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["resource_ids"]
        )
    if "layer_arns" in value:
        import capo_inspector2.types.string_filter_list

        out["layerArns"] = capo_inspector2.types.string_filter_list.serialize_json(
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
        import capo_inspector2.types.string_filter_list

        out["function_names"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["functionNames"]
            )
        )
    if "resourceIds" in data:
        import capo_inspector2.types.string_filter_list

        out["resource_ids"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["resourceIds"]
        )
    if "layerArns" in data:
        import capo_inspector2.types.string_filter_list

        out["layer_arns"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["layerArns"]
        )
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    return out
