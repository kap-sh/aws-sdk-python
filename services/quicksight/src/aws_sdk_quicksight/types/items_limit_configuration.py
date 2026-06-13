"""Generated from Smithy shape ``com.amazonaws.quicksight#ItemsLimitConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.long
    import aws_sdk_quicksight.types.other_categories


class ItemsLimitConfiguration(TypedDict):
    items_limit: NotRequired["aws_sdk_quicksight.types.long.Long"]
    """<p>The limit on how many items of a field are showed in the chart. For example, the number of slices that are displayed in a pie chart.</p>"""
    other_categories: NotRequired[
        "aws_sdk_quicksight.types.other_categories.OtherCategories"
    ]
    """<p>The <code>Show other</code> of an axis in the chart. Choose one of the following options:</p> <ul> <li> <p> <code>INCLUDE</code> </p> </li> <li> <p> <code>EXCLUDE</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ItemsLimitConfiguration) -> dict:
    out: dict = {}
    if "items_limit" in value:
        out["ItemsLimit"] = value["items_limit"]
    if "other_categories" in value:
        import aws_sdk_quicksight.types.other_categories

        out["OtherCategories"] = (
            aws_sdk_quicksight.types.other_categories.serialize_json(
                value["other_categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> ItemsLimitConfiguration:
    out: ItemsLimitConfiguration = {}  # type: ignore[typeddict-item]
    if "ItemsLimit" in data:
        out["items_limit"] = data["ItemsLimit"]
    if "OtherCategories" in data:
        import aws_sdk_quicksight.types.other_categories

        out["other_categories"] = (
            aws_sdk_quicksight.types.other_categories.deserialize_json(
                data["OtherCategories"]
            )
        )
    return out
