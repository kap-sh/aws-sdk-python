"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ListTablesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.max_results
    import aws_sdk_bcm_data_exports.types.next_page_token


class ListTablesRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_bcm_data_exports.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_bcm_data_exports.types.max_results.MaxResults"]
    """<p>The maximum number of objects that are returned for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTablesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTablesRequest:
    out: ListTablesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
