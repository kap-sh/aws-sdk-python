"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListLFTagExpressionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.page_size
    import capo_lakeformation.types.token


class ListLFTagExpressionsRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. </p>"""
    max_results: NotRequired["capo_lakeformation.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is not the first call to retrieve this list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLFTagExpressionsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLFTagExpressionsRequest:
    out: ListLFTagExpressionsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
