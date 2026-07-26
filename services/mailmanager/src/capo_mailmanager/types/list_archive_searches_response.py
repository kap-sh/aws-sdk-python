"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListArchiveSearchesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.pagination_token
    import capo_mailmanager.types.search_summary_list


class ListArchiveSearchesResponse(TypedDict, closed=True):
    searches: NotRequired[
        "capo_mailmanager.types.search_summary_list.SearchSummaryList"
    ]
    """<p>The list of search job identifiers and statuses.</p>"""
    next_token: NotRequired["capo_mailmanager.types.pagination_token.PaginationToken"]
    """<p>If present, use to retrieve the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListArchiveSearchesResponse) -> dict:
    out: dict = {}
    if "searches" in value:
        import capo_mailmanager.types.search_summary_list

        out["Searches"] = (
            capo_mailmanager.types.search_summary_list.serialize_aws_json_1_0(
                value["searches"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListArchiveSearchesResponse:
    out: ListArchiveSearchesResponse = {}  # type: ignore[typeddict-item]
    if "Searches" in data:
        import capo_mailmanager.types.search_summary_list

        out["searches"] = (
            capo_mailmanager.types.search_summary_list.deserialize_aws_json_1_0(
                data["Searches"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
