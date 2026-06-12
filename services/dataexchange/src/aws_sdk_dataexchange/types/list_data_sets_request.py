"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListDataSetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.max_results


class ListDataSetsRequest(TypedDict):
    max_results: "aws_sdk_dataexchange.types.max_results.MaxResults"
    """<p>The maximum number of results returned by a single call.</p>"""
    next_token: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""
    origin: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataSetsRequest:
    out: ListDataSetsRequest = {}  # type: ignore[typeddict-item]
    return out
