"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingFacet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.non_negative_count
    import aws_sdk_marketplace_discovery.types.nullable_string


class ListingFacet(TypedDict, closed=True):
    value: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The internal value used for filtering when passed back in a search filter.</p>"""
    display_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the facet value, suitable for display in a user interface.</p>"""
    parent: NotRequired[
        "aws_sdk_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>The parent facet value for hierarchical facets, such as subcategories.</p>"""
    count: "aws_sdk_marketplace_discovery.types.non_negative_count.NonNegativeCount"
    """<p>The number of listings matching this facet value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingFacet) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    out["displayName"] = value["display_name"]
    if "parent" in value:
        out["parent"] = value["parent"]
    out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> ListingFacet:
    out: ListingFacet = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("ListingFacet.value required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("ListingFacet.display_name required")
    if "parent" in data:
        out["parent"] = data["parent"]
    if "count" in data:
        out["count"] = data["count"]
    else:
        raise DeserializationError("ListingFacet.count required")
    return out
