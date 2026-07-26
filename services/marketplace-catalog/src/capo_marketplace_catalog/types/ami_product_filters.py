"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AmiProductFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.ami_product_entity_id_filter
    import capo_marketplace_catalog.types.ami_product_last_modified_date_filter
    import capo_marketplace_catalog.types.ami_product_title_filter
    import capo_marketplace_catalog.types.ami_product_visibility_filter


class AmiProductFilters(TypedDict, closed=True):
    entity_id: NotRequired[
        "capo_marketplace_catalog.types.ami_product_entity_id_filter.AmiProductEntityIdFilter"
    ]
    """<p>Unique identifier for the AMI product.</p>"""
    last_modified_date: NotRequired[
        "capo_marketplace_catalog.types.ami_product_last_modified_date_filter.AmiProductLastModifiedDateFilter"
    ]
    """<p>The last date on which the AMI product was modified.</p>"""
    product_title: NotRequired[
        "capo_marketplace_catalog.types.ami_product_title_filter.AmiProductTitleFilter"
    ]
    """<p>The title of the AMI product.</p>"""
    visibility: NotRequired[
        "capo_marketplace_catalog.types.ami_product_visibility_filter.AmiProductVisibilityFilter"
    ]
    """<p>The visibility of the AMI product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmiProductFilters) -> dict:
    out: dict = {}
    if "entity_id" in value:
        import capo_marketplace_catalog.types.ami_product_entity_id_filter

        out["EntityId"] = (
            capo_marketplace_catalog.types.ami_product_entity_id_filter.serialize_json(
                value["entity_id"]
            )
        )
    if "last_modified_date" in value:
        import capo_marketplace_catalog.types.ami_product_last_modified_date_filter

        out["LastModifiedDate"] = (
            capo_marketplace_catalog.types.ami_product_last_modified_date_filter.serialize_json(
                value["last_modified_date"]
            )
        )
    if "product_title" in value:
        import capo_marketplace_catalog.types.ami_product_title_filter

        out["ProductTitle"] = (
            capo_marketplace_catalog.types.ami_product_title_filter.serialize_json(
                value["product_title"]
            )
        )
    if "visibility" in value:
        import capo_marketplace_catalog.types.ami_product_visibility_filter

        out["Visibility"] = (
            capo_marketplace_catalog.types.ami_product_visibility_filter.serialize_json(
                value["visibility"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmiProductFilters:
    out: AmiProductFilters = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        import capo_marketplace_catalog.types.ami_product_entity_id_filter

        out["entity_id"] = (
            capo_marketplace_catalog.types.ami_product_entity_id_filter.deserialize_json(
                data["EntityId"]
            )
        )
    if "LastModifiedDate" in data:
        import capo_marketplace_catalog.types.ami_product_last_modified_date_filter

        out["last_modified_date"] = (
            capo_marketplace_catalog.types.ami_product_last_modified_date_filter.deserialize_json(
                data["LastModifiedDate"]
            )
        )
    if "ProductTitle" in data:
        import capo_marketplace_catalog.types.ami_product_title_filter

        out["product_title"] = (
            capo_marketplace_catalog.types.ami_product_title_filter.deserialize_json(
                data["ProductTitle"]
            )
        )
    if "Visibility" in data:
        import capo_marketplace_catalog.types.ami_product_visibility_filter

        out["visibility"] = (
            capo_marketplace_catalog.types.ami_product_visibility_filter.deserialize_json(
                data["Visibility"]
            )
        )
    return out
