"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerProductFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.container_product_entity_id_filter
    import aws_sdk_marketplace_catalog.types.container_product_last_modified_date_filter
    import aws_sdk_marketplace_catalog.types.container_product_title_filter
    import aws_sdk_marketplace_catalog.types.container_product_visibility_filter


class ContainerProductFilters(TypedDict):
    entity_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.container_product_entity_id_filter.ContainerProductEntityIdFilter"
    ]
    """<p>Unique identifier for the container product.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.container_product_last_modified_date_filter.ContainerProductLastModifiedDateFilter"
    ]
    """<p>The last date on which the container product was modified.</p>"""
    product_title: NotRequired[
        "aws_sdk_marketplace_catalog.types.container_product_title_filter.ContainerProductTitleFilter"
    ]
    """<p>The title of the container product.</p>"""
    visibility: NotRequired[
        "aws_sdk_marketplace_catalog.types.container_product_visibility_filter.ContainerProductVisibilityFilter"
    ]
    """<p>The visibility of the container product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProductFilters) -> dict:
    out: dict = {}
    if "entity_id" in value:
        import aws_sdk_marketplace_catalog.types.container_product_entity_id_filter

        out["EntityId"] = (
            aws_sdk_marketplace_catalog.types.container_product_entity_id_filter.serialize_json(
                value["entity_id"]
            )
        )
    if "last_modified_date" in value:
        import aws_sdk_marketplace_catalog.types.container_product_last_modified_date_filter

        out["LastModifiedDate"] = (
            aws_sdk_marketplace_catalog.types.container_product_last_modified_date_filter.serialize_json(
                value["last_modified_date"]
            )
        )
    if "product_title" in value:
        import aws_sdk_marketplace_catalog.types.container_product_title_filter

        out["ProductTitle"] = (
            aws_sdk_marketplace_catalog.types.container_product_title_filter.serialize_json(
                value["product_title"]
            )
        )
    if "visibility" in value:
        import aws_sdk_marketplace_catalog.types.container_product_visibility_filter

        out["Visibility"] = (
            aws_sdk_marketplace_catalog.types.container_product_visibility_filter.serialize_json(
                value["visibility"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContainerProductFilters:
    out: ContainerProductFilters = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        import aws_sdk_marketplace_catalog.types.container_product_entity_id_filter

        out["entity_id"] = (
            aws_sdk_marketplace_catalog.types.container_product_entity_id_filter.deserialize_json(
                data["EntityId"]
            )
        )
    if "LastModifiedDate" in data:
        import aws_sdk_marketplace_catalog.types.container_product_last_modified_date_filter

        out["last_modified_date"] = (
            aws_sdk_marketplace_catalog.types.container_product_last_modified_date_filter.deserialize_json(
                data["LastModifiedDate"]
            )
        )
    if "ProductTitle" in data:
        import aws_sdk_marketplace_catalog.types.container_product_title_filter

        out["product_title"] = (
            aws_sdk_marketplace_catalog.types.container_product_title_filter.deserialize_json(
                data["ProductTitle"]
            )
        )
    if "Visibility" in data:
        import aws_sdk_marketplace_catalog.types.container_product_visibility_filter

        out["visibility"] = (
            aws_sdk_marketplace_catalog.types.container_product_visibility_filter.deserialize_json(
                data["Visibility"]
            )
        )
    return out
