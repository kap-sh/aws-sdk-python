"""Generated from Smithy shape ``com.amazonaws.macie2#ListMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.max_results


class ListMembersRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_macie2.types.max_results.MaxResults"]
    """<p>The maximum number of items to include in each page of a paginated response.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""
    only_associated: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>Specifies which accounts to include in the response, based on the status of an account's relationship with the administrator account. By default, the response includes only current member accounts. To include all accounts, set this value to false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMembersRequest:
    out: ListMembersRequest = {}  # type: ignore[typeddict-item]
    return out
