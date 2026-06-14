"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#TabularConditions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.order_by_list
    import aws_sdk_iottwinmaker.types.property_filters


class TabularConditions(TypedDict):
    order_by: NotRequired["aws_sdk_iottwinmaker.types.order_by_list.OrderByList"]
    """<p>Filter criteria that orders the output. It can be sorted in ascending or descending order.</p>"""
    property_filters: NotRequired[
        "aws_sdk_iottwinmaker.types.property_filters.PropertyFilters"
    ]
    r"""<p>You can filter the request using various logical operators and a key-value format. For example:</p> <p> <code>{\"key\": \"serverType\", \"value\": \"webServer\"}</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TabularConditions) -> dict:
    out: dict = {}
    if "order_by" in value:
        import aws_sdk_iottwinmaker.types.order_by_list

        out["orderBy"] = aws_sdk_iottwinmaker.types.order_by_list.serialize_json(
            value["order_by"]
        )
    if "property_filters" in value:
        import aws_sdk_iottwinmaker.types.property_filters

        out["propertyFilters"] = (
            aws_sdk_iottwinmaker.types.property_filters.serialize_json(
                value["property_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> TabularConditions:
    out: TabularConditions = {}  # type: ignore[typeddict-item]
    if "orderBy" in data:
        import aws_sdk_iottwinmaker.types.order_by_list

        out["order_by"] = aws_sdk_iottwinmaker.types.order_by_list.deserialize_json(
            data["orderBy"]
        )
    if "propertyFilters" in data:
        import aws_sdk_iottwinmaker.types.property_filters

        out["property_filters"] = (
            aws_sdk_iottwinmaker.types.property_filters.deserialize_json(
                data["propertyFilters"]
            )
        )
    return out
