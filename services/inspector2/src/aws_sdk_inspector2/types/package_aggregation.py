"""Generated from Smithy shape ``com.amazonaws.inspector2#PackageAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.package_sort_by
    import aws_sdk_inspector2.types.sort_order
    import aws_sdk_inspector2.types.string_filter_list


class PackageAggregation(TypedDict):
    package_names: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The names of packages to aggregate findings on.</p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.sort_order.SortOrder"]
    """<p>The order to sort results by.</p>"""
    sort_by: NotRequired["aws_sdk_inspector2.types.package_sort_by.PackageSortBy"]
    """<p>The value to sort results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageAggregation) -> dict:
    out: dict = {}
    if "package_names" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["packageNames"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["package_names"]
            )
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    return out


def deserialize_json(data: dict) -> PackageAggregation:
    out: PackageAggregation = {}  # type: ignore[typeddict-item]
    if "packageNames" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["package_names"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["packageNames"]
            )
        )
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    return out
