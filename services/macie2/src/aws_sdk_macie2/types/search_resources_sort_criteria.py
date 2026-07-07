"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesSortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.order_by
    import aws_sdk_macie2.types.search_resources_sort_attribute_name


class SearchResourcesSortCriteria(TypedDict, closed=True):
    attribute_name: NotRequired[
        "aws_sdk_macie2.types.search_resources_sort_attribute_name.SearchResourcesSortAttributeName"
    ]
    """<p>The property to sort the results by.</p>"""
    order_by: NotRequired["aws_sdk_macie2.types.order_by.OrderBy"]
    """<p>The sort order to apply to the results, based on the value for the property specified by the attributeName property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesSortCriteria) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        import aws_sdk_macie2.types.search_resources_sort_attribute_name

        out["attributeName"] = (
            aws_sdk_macie2.types.search_resources_sort_attribute_name.serialize_json(
                value["attribute_name"]
            )
        )
    if "order_by" in value:
        import aws_sdk_macie2.types.order_by

        out["orderBy"] = aws_sdk_macie2.types.order_by.serialize_json(value["order_by"])
    return out


def deserialize_json(data: dict) -> SearchResourcesSortCriteria:
    out: SearchResourcesSortCriteria = {}  # type: ignore[typeddict-item]
    if "attributeName" in data:
        import aws_sdk_macie2.types.search_resources_sort_attribute_name

        out["attribute_name"] = (
            aws_sdk_macie2.types.search_resources_sort_attribute_name.deserialize_json(
                data["attributeName"]
            )
        )
    if "orderBy" in data:
        import aws_sdk_macie2.types.order_by

        out["order_by"] = aws_sdk_macie2.types.order_by.deserialize_json(
            data["orderBy"]
        )
    return out
