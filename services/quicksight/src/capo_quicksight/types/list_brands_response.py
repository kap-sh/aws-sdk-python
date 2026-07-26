"""Generated from Smithy shape ``com.amazonaws.quicksight#ListBrandsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.brand_summary_list
    import capo_quicksight.types.string


class ListBrandsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    brands: NotRequired["capo_quicksight.types.brand_summary_list.BrandSummaryList"]
    """<p>A list of all brands in your Amazon Web Services account. This structure provides basic information about each brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrandsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "brands" in value:
        import capo_quicksight.types.brand_summary_list

        out["Brands"] = capo_quicksight.types.brand_summary_list.serialize_json(
            value["brands"]
        )
    return out


def deserialize_json(data: dict) -> ListBrandsResponse:
    out: ListBrandsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Brands" in data:
        import capo_quicksight.types.brand_summary_list

        out["brands"] = capo_quicksight.types.brand_summary_list.deserialize_json(
            data["Brands"]
        )
    return out
