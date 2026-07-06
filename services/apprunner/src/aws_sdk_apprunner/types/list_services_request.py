"""Generated from Smithy shape ``com.amazonaws.apprunner#ListServicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.service_max_results
    import aws_sdk_apprunner.types.string


class ListServicesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>A token from a previous result page. Used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>"""
    max_results: NotRequired[
        "aws_sdk_apprunner.types.service_max_results.ServiceMaxResults"
    ]
    """<p>The maximum number of results to include in each response (result page). It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServicesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServicesRequest:
    out: ListServicesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
