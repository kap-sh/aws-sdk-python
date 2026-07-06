"""Generated from Smithy shape ``com.amazonaws.glue#ListColumnStatisticsTaskRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.page_size
    import aws_sdk_glue.types.token


class ListColumnStatisticsTaskRunsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_glue.types.page_size.PageSize"]
    """<p>The maximum size of the response.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListColumnStatisticsTaskRunsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListColumnStatisticsTaskRunsRequest:
    out: ListColumnStatisticsTaskRunsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
