"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Recommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.catalog_item
    import aws_sdk_customer_profiles.types.double0_to1


class Recommendation(TypedDict):
    catalog_item: NotRequired[
        "aws_sdk_customer_profiles.types.catalog_item.CatalogItem"
    ]
    """<p>The catalog item being recommended, including its complete details and attributes.</p>"""
    score: NotRequired["aws_sdk_customer_profiles.types.double0_to1.Double0To1"]
    """<p>Recommendation Score between 0 and 1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    if "catalog_item" in value:
        import aws_sdk_customer_profiles.types.catalog_item

        out["CatalogItem"] = (
            aws_sdk_customer_profiles.types.catalog_item.serialize_json(
                value["catalog_item"]
            )
        )
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if "CatalogItem" in data:
        import aws_sdk_customer_profiles.types.catalog_item

        out["catalog_item"] = (
            aws_sdk_customer_profiles.types.catalog_item.deserialize_json(
                data["CatalogItem"]
            )
        )
    if "Score" in data:
        out["score"] = data["Score"]
    return out
