"""Generated from Smithy shape ``com.amazonaws.quicksight#InnerFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.category_inner_filter


class InnerFilter(TypedDict):
    category_inner_filter: NotRequired[
        "aws_sdk_quicksight.types.category_inner_filter.CategoryInnerFilter"
    ]
    """<p>A <code>CategoryInnerFilter</code> filters text values for the <code>NestedFilter</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InnerFilter) -> dict:
    out: dict = {}
    if "category_inner_filter" in value:
        import aws_sdk_quicksight.types.category_inner_filter

        out["CategoryInnerFilter"] = (
            aws_sdk_quicksight.types.category_inner_filter.serialize_json(
                value["category_inner_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> InnerFilter:
    out: InnerFilter = {}  # type: ignore[typeddict-item]
    if "CategoryInnerFilter" in data:
        import aws_sdk_quicksight.types.category_inner_filter

        out["category_inner_filter"] = (
            aws_sdk_quicksight.types.category_inner_filter.deserialize_json(
                data["CategoryInnerFilter"]
            )
        )
    return out
