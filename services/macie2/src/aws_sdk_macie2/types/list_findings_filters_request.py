"""Generated from Smithy shape ``com.amazonaws.macie2#ListFindingsFiltersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.max_results


class ListFindingsFiltersRequest(TypedDict):
    max_results: NotRequired["aws_sdk_macie2.types.max_results.MaxResults"]
    """<p>The maximum number of items to include in each page of a paginated response.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsFiltersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFindingsFiltersRequest:
    out: ListFindingsFiltersRequest = {}  # type: ignore[typeddict-item]
    return out
