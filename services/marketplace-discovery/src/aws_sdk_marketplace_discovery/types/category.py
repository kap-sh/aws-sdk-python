"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#Category``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.non_empty_string


class Category(TypedDict):
    category_id: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The machine-readable identifier of the category.</p>"""
    display_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the category.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Category) -> dict:
    out: dict = {}
    out["categoryId"] = value["category_id"]
    out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> Category:
    out: Category = {}  # type: ignore[typeddict-item]
    if "categoryId" in data:
        out["category_id"] = data["categoryId"]
    else:
        raise DeserializationError("Category.category_id required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("Category.display_name required")
    return out
