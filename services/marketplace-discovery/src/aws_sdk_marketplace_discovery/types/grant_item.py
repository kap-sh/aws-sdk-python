"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GrantItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.bounded_string
    import aws_sdk_marketplace_discovery.types.dimension_label_list


class GrantItem(TypedDict, closed=True):
    dimension_key: "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The machine-readable key identifying the entitlement dimension.</p>"""
    display_name: "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The human-readable name of the entitlement dimension.</p>"""
    description: NotRequired[
        "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    ]
    """<p>A description of the entitlement.</p>"""
    dimension_labels: NotRequired[
        "aws_sdk_marketplace_discovery.types.dimension_label_list.DimensionLabelList"
    ]
    """<p>Labels used to categorize this entitlement, such as by region.</p>"""
    unit: "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The unit of measurement for the entitlement.</p>"""
    max_quantity: NotRequired["int"]
    """<p>The maximum quantity of the entitlement that can be granted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrantItem) -> dict:
    out: dict = {}
    out["dimensionKey"] = value["dimension_key"]
    out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "dimension_labels" in value:
        import aws_sdk_marketplace_discovery.types.dimension_label_list

        out["dimensionLabels"] = (
            aws_sdk_marketplace_discovery.types.dimension_label_list.serialize_json(
                value["dimension_labels"]
            )
        )
    out["unit"] = value["unit"]
    if "max_quantity" in value:
        out["maxQuantity"] = value["max_quantity"]
    return out


def deserialize_json(data: dict) -> GrantItem:
    out: GrantItem = {}  # type: ignore[typeddict-item]
    if "dimensionKey" in data:
        out["dimension_key"] = data["dimensionKey"]
    else:
        raise DeserializationError("GrantItem.dimension_key required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("GrantItem.display_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "dimensionLabels" in data:
        import aws_sdk_marketplace_discovery.types.dimension_label_list

        out["dimension_labels"] = (
            aws_sdk_marketplace_discovery.types.dimension_label_list.deserialize_json(
                data["dimensionLabels"]
            )
        )
    if "unit" in data:
        out["unit"] = data["unit"]
    else:
        raise DeserializationError("GrantItem.unit required")
    if "maxQuantity" in data:
        out["max_quantity"] = data["maxQuantity"]
    return out
