"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxEnvironmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.boxed_integer
    import aws_sdk_finspace.types.pagination_token


class ListKxEnvironmentsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""
    max_results: NotRequired["aws_sdk_finspace.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of results to return in this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxEnvironmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKxEnvironmentsRequest:
    out: ListKxEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    return out
