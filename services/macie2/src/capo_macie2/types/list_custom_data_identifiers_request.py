"""Generated from Smithy shape ``com.amazonaws.macie2#ListCustomDataIdentifiersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__integer
    import capo_macie2.types.__string


class ListCustomDataIdentifiersRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_macie2.types.__integer.__integer"]
    """<p>The maximum number of items to include in each page of the response.</p>"""
    next_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomDataIdentifiersRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomDataIdentifiersRequest:
    out: ListCustomDataIdentifiersRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
