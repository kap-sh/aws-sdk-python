"""Generated from Smithy shape ``com.amazonaws.amp#ListScrapersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.pagination_token
    import capo_amp.types.scraper_summary_list


class ListScrapersResponse(TypedDict, closed=True):
    scrapers: "capo_amp.types.scraper_summary_list.ScraperSummaryList"
    """<p>A list of <code>ScraperSummary</code> structures giving information about scrapers in the account that match the filters provided.</p>"""
    next_token: NotRequired["capo_amp.types.pagination_token.PaginationToken"]
    """<p>A token indicating that there are more results to retrieve. You can use this token as part of your next <code>ListScrapers</code> operation to retrieve those results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScrapersResponse) -> dict:
    out: dict = {}
    import capo_amp.types.scraper_summary_list

    out["scrapers"] = capo_amp.types.scraper_summary_list.serialize_json(
        value["scrapers"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListScrapersResponse:
    out: ListScrapersResponse = {}  # type: ignore[typeddict-item]
    if "scrapers" in data:
        import capo_amp.types.scraper_summary_list

        out["scrapers"] = capo_amp.types.scraper_summary_list.deserialize_json(
            data["scrapers"]
        )
    else:
        raise DeserializationError("ListScrapersResponse.scrapers required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
