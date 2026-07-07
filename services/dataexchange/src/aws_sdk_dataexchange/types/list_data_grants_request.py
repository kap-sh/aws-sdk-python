"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListDataGrantsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.max_results


class ListDataGrantsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_dataexchange.types.max_results.MaxResults"]
    """<p>The maximum number of results to be included in the next page.</p>"""
    next_token: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataGrantsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataGrantsRequest:
    out: ListDataGrantsRequest = {}  # type: ignore[typeddict-item]
    return out
