"""Generated from Smithy shape ``com.amazonaws.omics#ListVariantStoresRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.id_list
    import aws_sdk_omics.types.list_variant_stores_filter


class ListVariantStoresRequest(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of stores to return in one page of results.</p>"""
    ids: NotRequired["aws_sdk_omics.types.id_list.IdList"]
    """<p>A list of store IDs.</p>"""
    next_token: NotRequired["str"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    filter: NotRequired[
        "aws_sdk_omics.types.list_variant_stores_filter.ListVariantStoresFilter"
    ]
    """<p>A filter to apply to the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVariantStoresRequest) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_omics.types.id_list

        out["ids"] = aws_sdk_omics.types.id_list.serialize_json(value["ids"])
    if "filter" in value:
        import aws_sdk_omics.types.list_variant_stores_filter

        out["filter"] = aws_sdk_omics.types.list_variant_stores_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ListVariantStoresRequest:
    out: ListVariantStoresRequest = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_omics.types.id_list

        out["ids"] = aws_sdk_omics.types.id_list.deserialize_json(data["ids"])
    if "filter" in data:
        import aws_sdk_omics.types.list_variant_stores_filter

        out["filter"] = aws_sdk_omics.types.list_variant_stores_filter.deserialize_json(
            data["filter"]
        )
    return out
