"""Generated from Smithy shape ``com.amazonaws.mediatailor#ListPrefetchSchedulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__list_of_prefetch_schedule
    import capo_mediatailor.types.__string


class ListPrefetchSchedulesResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mediatailor.types.__list_of_prefetch_schedule.__listOfPrefetchSchedule"
    ]
    """<p>Lists the prefetch schedules. An empty <code>Items</code> list doesn't mean there aren't more items to fetch, just that that page was empty.</p>"""
    next_token: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrefetchSchedulesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mediatailor.types.__list_of_prefetch_schedule

        out["Items"] = (
            capo_mediatailor.types.__list_of_prefetch_schedule.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPrefetchSchedulesResponse:
    out: ListPrefetchSchedulesResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_mediatailor.types.__list_of_prefetch_schedule

        out["items"] = (
            capo_mediatailor.types.__list_of_prefetch_schedule.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
