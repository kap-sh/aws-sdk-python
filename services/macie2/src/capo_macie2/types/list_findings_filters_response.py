"""Generated from Smithy shape ``com.amazonaws.macie2#ListFindingsFiltersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_findings_filter_list_item
    import capo_macie2.types.__string


class ListFindingsFiltersResponse(TypedDict, closed=True):
    findings_filter_list_items: NotRequired[
        "capo_macie2.types.__list_of_findings_filter_list_item.__listOfFindingsFilterListItem"
    ]
    """<p>An array of objects, one for each filter that's associated with the account.</p>"""
    next_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsFiltersResponse) -> dict:
    out: dict = {}
    if "findings_filter_list_items" in value:
        import capo_macie2.types.__list_of_findings_filter_list_item

        out["findingsFilterListItems"] = (
            capo_macie2.types.__list_of_findings_filter_list_item.serialize_json(
                value["findings_filter_list_items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingsFiltersResponse:
    out: ListFindingsFiltersResponse = {}  # type: ignore[typeddict-item]
    if "findingsFilterListItems" in data:
        import capo_macie2.types.__list_of_findings_filter_list_item

        out["findings_filter_list_items"] = (
            capo_macie2.types.__list_of_findings_filter_list_item.deserialize_json(
                data["findingsFilterListItems"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
