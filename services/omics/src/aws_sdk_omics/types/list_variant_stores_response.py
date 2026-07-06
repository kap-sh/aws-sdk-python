"""Generated from Smithy shape ``com.amazonaws.omics#ListVariantStoresResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.variant_store_items


class ListVariantStoresResponse(TypedDict, closed=True):
    variant_stores: NotRequired[
        "aws_sdk_omics.types.variant_store_items.VariantStoreItems"
    ]
    """<p>A list of variant stores.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVariantStoresResponse) -> dict:
    out: dict = {}
    if "variant_stores" in value:
        import aws_sdk_omics.types.variant_store_items

        out["variantStores"] = aws_sdk_omics.types.variant_store_items.serialize_json(
            value["variant_stores"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVariantStoresResponse:
    out: ListVariantStoresResponse = {}  # type: ignore[typeddict-item]
    if "variantStores" in data:
        import aws_sdk_omics.types.variant_store_items

        out["variant_stores"] = (
            aws_sdk_omics.types.variant_store_items.deserialize_json(
                data["variantStores"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
