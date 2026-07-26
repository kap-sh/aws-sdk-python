"""Generated from Smithy shape ``com.amazonaws.glue#GetSecurityConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_string
    import capo_glue.types.page_size


class GetSecurityConfigurationsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSecurityConfigurationsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSecurityConfigurationsRequest:
    out: GetSecurityConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
