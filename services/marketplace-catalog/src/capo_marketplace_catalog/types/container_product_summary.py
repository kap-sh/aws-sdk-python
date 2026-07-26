"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerProductSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.container_product_title_string
    import capo_marketplace_catalog.types.container_product_visibility_string


class ContainerProductSummary(TypedDict, closed=True):
    product_title: NotRequired[
        "capo_marketplace_catalog.types.container_product_title_string.ContainerProductTitleString"
    ]
    """<p>The title of the container product.</p>"""
    visibility: NotRequired[
        "capo_marketplace_catalog.types.container_product_visibility_string.ContainerProductVisibilityString"
    ]
    """<p>The lifecycle of the product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProductSummary) -> dict:
    out: dict = {}
    if "product_title" in value:
        out["ProductTitle"] = value["product_title"]
    if "visibility" in value:
        import capo_marketplace_catalog.types.container_product_visibility_string

        out["Visibility"] = (
            capo_marketplace_catalog.types.container_product_visibility_string.serialize_json(
                value["visibility"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContainerProductSummary:
    out: ContainerProductSummary = {}  # type: ignore[typeddict-item]
    if "ProductTitle" in data:
        out["product_title"] = data["ProductTitle"]
    if "Visibility" in data:
        import capo_marketplace_catalog.types.container_product_visibility_string

        out["visibility"] = (
            capo_marketplace_catalog.types.container_product_visibility_string.deserialize_json(
                data["Visibility"]
            )
        )
    return out
