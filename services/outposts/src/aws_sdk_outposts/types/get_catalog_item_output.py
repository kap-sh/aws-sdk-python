"""Generated from Smithy shape ``com.amazonaws.outposts#GetCatalogItemOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.catalog_item


class GetCatalogItemOutput(TypedDict):
    catalog_item: NotRequired["aws_sdk_outposts.types.catalog_item.CatalogItem"]
    """<p>Information about this catalog item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCatalogItemOutput) -> dict:
    out: dict = {}
    if "catalog_item" in value:
        import aws_sdk_outposts.types.catalog_item

        out["CatalogItem"] = aws_sdk_outposts.types.catalog_item.serialize_json(
            value["catalog_item"]
        )
    return out


def deserialize_json(data: dict) -> GetCatalogItemOutput:
    out: GetCatalogItemOutput = {}  # type: ignore[typeddict-item]
    if "CatalogItem" in data:
        import aws_sdk_outposts.types.catalog_item

        out["catalog_item"] = aws_sdk_outposts.types.catalog_item.deserialize_json(
            data["CatalogItem"]
        )
    return out
