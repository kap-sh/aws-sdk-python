"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#RateCardItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.bounded_string
    import aws_sdk_marketplace_discovery.types.dimension_label_list


class RateCardItem(TypedDict):
    dimension_key: "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The machine-readable key identifying the dimension being priced.</p>"""
    display_name: "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The human-readable name of the dimension.</p>"""
    description: NotRequired[
        "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    ]
    """<p>A description of the dimension being priced.</p>"""
    dimension_labels: NotRequired[
        "aws_sdk_marketplace_discovery.types.dimension_label_list.DimensionLabelList"
    ]
    """<p>Labels used to categorize this dimension, such as by region.</p>"""
    unit: "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The unit of measurement for the dimension.</p>"""
    price: "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The price per unit for the dimension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RateCardItem) -> dict:
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
    out["price"] = value["price"]
    return out


def deserialize_json(data: dict) -> RateCardItem:
    out: RateCardItem = {}  # type: ignore[typeddict-item]
    if "dimensionKey" in data:
        out["dimension_key"] = data["dimensionKey"]
    else:
        raise DeserializationError("RateCardItem.dimension_key required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("RateCardItem.display_name required")
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
        raise DeserializationError("RateCardItem.unit required")
    if "price" in data:
        out["price"] = data["price"]
    else:
        raise DeserializationError("RateCardItem.price required")
    return out
