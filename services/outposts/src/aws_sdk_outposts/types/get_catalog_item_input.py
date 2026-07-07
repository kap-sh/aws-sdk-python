"""Generated from Smithy shape ``com.amazonaws.outposts#GetCatalogItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.sku_code


class GetCatalogItemInput(TypedDict, closed=True):
    catalog_item_id: "aws_sdk_outposts.types.sku_code.SkuCode"
    """<p>The ID of the catalog item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCatalogItemInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCatalogItemInput:
    out: GetCatalogItemInput = {}  # type: ignore[typeddict-item]
    return out
