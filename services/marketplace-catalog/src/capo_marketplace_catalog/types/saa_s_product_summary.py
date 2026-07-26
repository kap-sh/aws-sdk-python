"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SaaSProductSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.saa_s_product_title_string
    import capo_marketplace_catalog.types.saa_s_product_visibility_string


class SaaSProductSummary(TypedDict, closed=True):
    product_title: NotRequired[
        "capo_marketplace_catalog.types.saa_s_product_title_string.SaaSProductTitleString"
    ]
    """<p>The title of the SaaS product.</p>"""
    visibility: NotRequired[
        "capo_marketplace_catalog.types.saa_s_product_visibility_string.SaaSProductVisibilityString"
    ]
    """<p>The lifecycle of the SaaS product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaaSProductSummary) -> dict:
    out: dict = {}
    if "product_title" in value:
        out["ProductTitle"] = value["product_title"]
    if "visibility" in value:
        import capo_marketplace_catalog.types.saa_s_product_visibility_string

        out["Visibility"] = (
            capo_marketplace_catalog.types.saa_s_product_visibility_string.serialize_json(
                value["visibility"]
            )
        )
    return out


def deserialize_json(data: dict) -> SaaSProductSummary:
    out: SaaSProductSummary = {}  # type: ignore[typeddict-item]
    if "ProductTitle" in data:
        out["product_title"] = data["ProductTitle"]
    if "Visibility" in data:
        import capo_marketplace_catalog.types.saa_s_product_visibility_string

        out["visibility"] = (
            capo_marketplace_catalog.types.saa_s_product_visibility_string.deserialize_json(
                data["Visibility"]
            )
        )
    return out
