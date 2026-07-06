"""Generated from Smithy shape ``com.amazonaws.outposts#ListCatalogItemsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.catalog_item_list_definition
    import aws_sdk_outposts.types.token


class ListCatalogItemsOutput(TypedDict, closed=True):
    catalog_items: NotRequired[
        "aws_sdk_outposts.types.catalog_item_list_definition.CatalogItemListDefinition"
    ]
    """<p>Information about the catalog items.</p>"""
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: ListCatalogItemsOutput) -> dict:
    out: dict = {}
    if "catalog_items" in value:
        import aws_sdk_outposts.types.catalog_item_list_definition

        out["CatalogItems"] = (
            aws_sdk_outposts.types.catalog_item_list_definition.serialize_json(
                value["catalog_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCatalogItemsOutput:
    out: ListCatalogItemsOutput = {}  # type: ignore[typeddict-item]
    if "CatalogItems" in data:
        import aws_sdk_outposts.types.catalog_item_list_definition

        out["catalog_items"] = (
            aws_sdk_outposts.types.catalog_item_list_definition.deserialize_json(
                data["CatalogItems"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
