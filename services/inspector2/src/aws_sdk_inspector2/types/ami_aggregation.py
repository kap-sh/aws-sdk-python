"""Generated from Smithy shape ``com.amazonaws.inspector2#AmiAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.ami_sort_by
    import aws_sdk_inspector2.types.sort_order
    import aws_sdk_inspector2.types.string_filter_list


class AmiAggregation(TypedDict, closed=True):
    amis: NotRequired["aws_sdk_inspector2.types.string_filter_list.StringFilterList"]
    """<p>The IDs of AMIs to aggregate findings for.</p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.sort_order.SortOrder"]
    """<p>The order to sort results by.</p>"""
    sort_by: NotRequired["aws_sdk_inspector2.types.ami_sort_by.AmiSortBy"]
    """<p>The value to sort results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmiAggregation) -> dict:
    out: dict = {}
    if "amis" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["amis"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["amis"]
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    return out


def deserialize_json(data: dict) -> AmiAggregation:
    out: AmiAggregation = {}  # type: ignore[typeddict-item]
    if "amis" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["amis"] = aws_sdk_inspector2.types.string_filter_list.deserialize_json(
            data["amis"]
        )
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    return out
