"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ListExportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.max_results
    import capo_bcm_data_exports.types.next_page_token


class ListExportsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_bcm_data_exports.types.max_results.MaxResults"]
    """<p>The maximum number of objects that are returned for the request.</p>"""
    next_token: NotRequired["capo_bcm_data_exports.types.next_page_token.NextPageToken"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExportsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExportsRequest:
    out: ListExportsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
