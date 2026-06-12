"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SaaSProductFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.saa_s_product_entity_id_filter
    import aws_sdk_marketplace_catalog.types.saa_s_product_last_modified_date_filter
    import aws_sdk_marketplace_catalog.types.saa_s_product_title_filter
    import aws_sdk_marketplace_catalog.types.saa_s_product_visibility_filter


class SaaSProductFilters(TypedDict):
    entity_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.saa_s_product_entity_id_filter.SaaSProductEntityIdFilter"
    ]
    """<p>Unique identifier for the SaaS product.</p>"""
    product_title: NotRequired[
        "aws_sdk_marketplace_catalog.types.saa_s_product_title_filter.SaaSProductTitleFilter"
    ]
    """<p>The title of the SaaS product.</p>"""
    visibility: NotRequired[
        "aws_sdk_marketplace_catalog.types.saa_s_product_visibility_filter.SaaSProductVisibilityFilter"
    ]
    """<p>The visibility of the SaaS product.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.saa_s_product_last_modified_date_filter.SaaSProductLastModifiedDateFilter"
    ]
    """<p>The last date on which the SaaS product was modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaaSProductFilters) -> dict:
    out: dict = {}
    if "entity_id" in value:
        import aws_sdk_marketplace_catalog.types.saa_s_product_entity_id_filter

        out["EntityId"] = (
            aws_sdk_marketplace_catalog.types.saa_s_product_entity_id_filter.serialize_json(
                value["entity_id"]
            )
        )
    if "product_title" in value:
        import aws_sdk_marketplace_catalog.types.saa_s_product_title_filter

        out["ProductTitle"] = (
            aws_sdk_marketplace_catalog.types.saa_s_product_title_filter.serialize_json(
                value["product_title"]
            )
        )
    if "visibility" in value:
        import aws_sdk_marketplace_catalog.types.saa_s_product_visibility_filter

        out["Visibility"] = (
            aws_sdk_marketplace_catalog.types.saa_s_product_visibility_filter.serialize_json(
                value["visibility"]
            )
        )
    if "last_modified_date" in value:
        import aws_sdk_marketplace_catalog.types.saa_s_product_last_modified_date_filter

        out["LastModifiedDate"] = (
            aws_sdk_marketplace_catalog.types.saa_s_product_last_modified_date_filter.serialize_json(
                value["last_modified_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> SaaSProductFilters:
    out: SaaSProductFilters = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        import aws_sdk_marketplace_catalog.types.saa_s_product_entity_id_filter

        out["entity_id"] = (
            aws_sdk_marketplace_catalog.types.saa_s_product_entity_id_filter.deserialize_json(
                data["EntityId"]
            )
        )
    if "ProductTitle" in data:
        import aws_sdk_marketplace_catalog.types.saa_s_product_title_filter

        out["product_title"] = (
            aws_sdk_marketplace_catalog.types.saa_s_product_title_filter.deserialize_json(
                data["ProductTitle"]
            )
        )
    if "Visibility" in data:
        import aws_sdk_marketplace_catalog.types.saa_s_product_visibility_filter

        out["visibility"] = (
            aws_sdk_marketplace_catalog.types.saa_s_product_visibility_filter.deserialize_json(
                data["Visibility"]
            )
        )
    if "LastModifiedDate" in data:
        import aws_sdk_marketplace_catalog.types.saa_s_product_last_modified_date_filter

        out["last_modified_date"] = (
            aws_sdk_marketplace_catalog.types.saa_s_product_last_modified_date_filter.deserialize_json(
                data["LastModifiedDate"]
            )
        )
    return out
