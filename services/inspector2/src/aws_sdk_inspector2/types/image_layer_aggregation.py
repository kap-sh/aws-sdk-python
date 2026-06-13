"""Generated from Smithy shape ``com.amazonaws.inspector2#ImageLayerAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.image_layer_sort_by
    import aws_sdk_inspector2.types.sort_order
    import aws_sdk_inspector2.types.string_filter_list


class ImageLayerAggregation(TypedDict):
    repositories: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The repository associated with the container image hosting the layers.</p>"""
    resource_ids: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The ID of the container image layer.</p>"""
    layer_hashes: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The hashes associated with the layers.</p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.sort_order.SortOrder"]
    """<p>The order to sort results by.</p>"""
    sort_by: NotRequired[
        "aws_sdk_inspector2.types.image_layer_sort_by.ImageLayerSortBy"
    ]
    """<p>The value to sort results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageLayerAggregation) -> dict:
    out: dict = {}
    if "repositories" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["repositories"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["repositories"]
            )
        )
    if "resource_ids" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["resourceIds"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["resource_ids"]
        )
    if "layer_hashes" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["layerHashes"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["layer_hashes"]
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    return out


def deserialize_json(data: dict) -> ImageLayerAggregation:
    out: ImageLayerAggregation = {}  # type: ignore[typeddict-item]
    if "repositories" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["repositories"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["repositories"]
            )
        )
    if "resourceIds" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["resource_ids"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["resourceIds"]
            )
        )
    if "layerHashes" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["layer_hashes"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["layerHashes"]
            )
        )
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    return out
